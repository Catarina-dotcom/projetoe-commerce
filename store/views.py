from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail


def _get_cart_session(request):
    """
    Recupera o carrinho da sessão.
    Estrutura: {'product_id': quantidade, ...}
    """
    cart = request.session.get('cart', {})
    return cart

def _save_cart_session(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    cart = _get_cart_session(request)
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    _save_cart_session(request, cart)
    return redirect('store:view_cart')
def remove_from_cart(request, product_id):
    cart = _get_cart_session(request)
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]

    _save_cart_session(request, cart)
    return redirect('store:view_cart')

def view_cart(request):
    cart = _get_cart_session(request)

    cart_items = []
    total = 0

    for product_id_str, quantity in cart.items():
        product = Product.objects.filter(id=int(product_id_str)).first()
        if not product:
            continue
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'store/cart.html', context)
def update_cart(request, product_id):
    cart = _get_cart_session(request)
    product_id_str = str(product_id)

    if request.method == "POST":
        new_quantity = int(request.POST.get("quantity", 1))

        if new_quantity > 0:
            cart[product_id_str] = new_quantity
        else:
            
            if product_id_str in cart:
                del cart[product_id_str]

        _save_cart_session(request, cart)

    return redirect('store:view_cart')
def product_list(request):
    order = request.GET.get('order', '')
    products = Product.objects.filter(available=True)

    
    if order == 'preco_asc':
        products = products.order_by('price')
    elif order == 'preco_desc':
        products = products.order_by('-price')
    elif order == 'novidade':
        products = products.order_by('-created_at')

 
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/product_list.html', {'page_obj': page_obj, 'order': order})
def informacoes(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        # Aqui você pode salvar no banco ou enviar por email
        messages.success(request, "Mensagem enviada com sucesso!")

    return render(request, 'store/informacoes.html')