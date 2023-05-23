from .models import Account
from store.models import Product, Cart, CartItem
from rest_framework import generics
from authentication.api.serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from store.utils import get_cart
from .tokens import account_activation_token


# Create your views here.
class CreateUser(generics.CreateAPIView):
    serializer_class = AccountSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        headers = self.get_success_headers(serializer.data)
        response_data = {
            "activation_sent": serializer.context.get('activation_mail'),
            "user_id": user.id,
        }
        return Response(response_data, status=HTTP_201_CREATED, headers=headers)


class ActivateUser(generics.UpdateAPIView):
    serializer_class = AccountSerializer

    def get(request, uidb64, token):
        message = None
        message_type = None
        redirect = None
        success = False

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            if request.user.is_authenticated:
                message = 'You cannot authenticate an account while logged in'
                message_type = 'warning'
                redirect = 'home'
            elif user.is_active == True:
                message = 'This account has been activated already'
                message_type = 'warning'
                redirect = 'home'
            else:
                user.is_active = True
                user.save()
                cart = Cart.objects.get_or_create(user=user)[0]
                cart.save()

                message = 'Your account has been successfully activated'
                message_type = 'success'

                session_cart = get_cart(request.session)
                cart_list = list(session_cart.keys())
                if len(cart_list) > 0:
                    for id in cart_list:
                        quantity = int(session_cart[id]['quantity'])
                        try:
                            product = Product.objects.get(id=int(id))
                            detailed_cart = CartItem.objects.create(
                                product = product,
                                cart = cart,
                                quantity = quantity,
                            )
                            detailed_cart.save()
                        except ObjectDoesNotExist:
                            message = 'A product in your cart does not exist anymore'
                            message_type = 'error'
                    message = 'Your cart has been synced into your account'
                    message_type = 'success'

                redirect = 'home'
                success = True
        else:
            message = 'Activation Link is Invalid'
            message_type = 'error'
            redirect = 'home'

        return {
            "success": success,
            'message': message,
            'message_type': message_type,
            "redirect": redirect
        }


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user