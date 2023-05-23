import json
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .models import Cart, CartItem

def get_cart(session):
    cart = session.get("user-cart")
    if cart == None:
        cart = json.dumps({})
        session["user-cart"] = cart
    return json.loads(cart)


def add_to_cart(request, product, quantity):
    quantity = int(quantity)
    # product_exists = Cart.cart_products.get(product)
    user = request.user
    product_id = product.id
    if user.is_authenticated:
        user_cart = Cart.objects.get(user=user)
        # user_wishlist = Wishlist.objects.get_or_create(user=user)[0]
        try:
            products = user_cart.cart_products.get(id=product.id)
        except MultipleObjectsReturned:
            all_duplicated = user_cart.cart_products.filter(id=product.id)[1:]
            for item in all_duplicated:
                user_cart.cart_products.remove(item)
            message = "Multiple items found in your cart. Deleting Now."
            message_type = "info"
        except ObjectDoesNotExist:
            detailed_cart = CartItem.objects.create(
                cart = user_cart,
                product = product,
                quantity = quantity,
            )
            detailed_cart.save()
            message = "Item added to cart"
            message_type = "success"
        else:
            complete_cart = CartItem.objects.get(cart=user_cart, product=product)
            complete_cart.quantity += quantity
            complete_cart.save()
            quantity = complete_cart.quantity
            message = "Cart Updated Successfully"
            message_type = "success"
    else:
        user_cart = get_cart(request.session)
        
        if str(product_id) in user_cart:
            item = user_cart[str(product_id)]
            item_quantity = int(item["quantity"])
            item["quantity"] = str(item_quantity + quantity)
            message = "Cart Item Updated"
            quantity = item["quantity"]
        else:
            user_cart[int(product_id)] = {"quantity": quantity}
            message = "Item Added To Cart"
        request.session['user-cart'] = json.dumps(user_cart)
        message_type = "success"

    return message, message_type