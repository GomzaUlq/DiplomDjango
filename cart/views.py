from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Cart, CartItem


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1
        request.session['cart'] = cart

    return redirect('showcase')


@login_required
def view_cart(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        items = cart.items.all()
        total_price = sum(item.product.price * item.quantity for item in items)
    else:
        cart = request.session.get('cart', {})
        items = []
        total_price = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            items.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity

    return render(request, 'cart/cart_view.html', {'items': items, 'total_price': total_price})


@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        if new_quantity.isdigit() and int(new_quantity) > 0:
            cart_item.quantity = int(new_quantity)
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        cart_items = cart.items.all()
        cart_items.delete()
        messages.success(request, "Заказ успешно оформлен")
        return render(request, 'cart/checkout.html', {'items': cart_items, 'total_price': 0})
    cart_items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/checkout.html', {'items': cart_items, 'total_price': total_price})
