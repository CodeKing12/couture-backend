from rest_framework.serializers import ModelSerializer
from authentication.models import Account
from the_pot_shop_backend.utils import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.conf import settings
from authentication.tokens import account_activation_token


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        # I excluded both info because drf tries to manually populate them during user creation which throws a Direct Assignment error.
        # If you want to include both groups and user_permissions in the returned serialized data, you can create a RegistrationSerializer that excludes them during user creation and then remove them from the exclude list in this AccountSerializer.
        exclude = ['groups', 'user_permissions']
        # include = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'write_only': True},
        }

    def create(self, validated_data):
        activation_mail = False
        user = Account.objects.create_user(**validated_data)

        # Generate an activation key
        activation_key = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        # Send the activation email
        mail_subject = 'Activate your account'
        activation_url = reverse('activate_user', args=[activation_key, token])
        activation_url = self.context['request'].build_absolute_uri(activation_url)
        message = render_to_string('authentication/activation_email.html', {
            'user': user,
            'activation_url': activation_url,
        })
        to = [
            {
                "email": user.email,
                "name": f"{user.first_name} {user.last_name}"
            }
        ]
        mail_response = send_mail('welcome@thepotshop.com', mail_subject, message, to)
        if (mail_response['status'] == "success"):
            activation_mail = True

        self.context['activation_mail'] = activation_mail
        print(activation_url)

        return user