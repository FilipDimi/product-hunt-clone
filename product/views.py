from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'product/index.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.POST['icon'] and request.POST['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.pubDate = timezone.datetime.now()
            product.icon = request.POST['icon']
            product.image = request.POST['image']
            product.hunter = request.user

            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                product.url = request.POST['url']
            else:
                product.url = "http://{}".format(request.POST['url'])

            product.save()
            return redirect('home')
        else:
            return render(request, 'product/create.html', {"error":"All fields are required!"})
    else:
        return render(request, 'product/create.html')
