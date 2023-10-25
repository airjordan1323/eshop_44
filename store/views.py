from django.shortcuts import render, redirect
from .models import Category, Products, Cart
from .forms import RegistrationForm
from telebot import TeleBot
from django.conf import settings

bot = TeleBot(settings.BOT_TOKEN)


def home(request):
    all_cat = Category.objects.all()
    all_prod = Products.objects.all()
    if request.GET.get('search_pr'):
        all_prod = Products.objects.filter(name__icontains=request.GET.get('search_pr'))
    context = {'all_products': all_prod,
               'all_categories': all_cat}

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contacts.html')


def get_all_products(request, pk):
    category = Category.objects.get(id=pk)
    products = Products.objects.filter(category=category)

    context = {'products': products}
    return render(request, 'all_products.html', context)


def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity'))
    prod = Products.objects.get(id=product_id)
    Cart.objects.create(
        user_id=request.user.id,
        product_id=prod,
        count=quantity
    )
    return redirect('/')


def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product.html', context)


def user_cart(request):
    user = request.user.id
    cart = Cart.objects.filter(user_id=user)
    if request.method == 'POST':
        message_text = "Продукты: \n\n"
        for i in cart:
            message_text += f'Название товара: {i.product_id.name}\n'
            message_text += f'Количество: {i.count}\n'
        bot.send_message(chat_id=1380637770, text=message_text)
        cart.delete()
        return redirect('/')
    context = {'cart_list': cart}
    return render(request, 'user_cart.html', context)


def del_item(request, cart_id):
    Cart.objects.get(user_id=request.user.id, id=cart_id).delete()
    return redirect('/my-cart/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'registration/register.html', context)
