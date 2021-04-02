from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Post, Cart
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'store/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'store/post_detail.html', {'post': post})

def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    return render(request, 'store/shopping_cart.html', context)

def update_cart(request, pk):
    cart = Cart.objects.all()[0]
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        pass
    except:
        pass
    if not post in cart.posts.all():
        cart.posts.add(post)
    else:
        cart.posts.remove(post)

    new_total = 0.00
    for item in cart.posts.all():
        new_total += float(item.price)

    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart"))
