from django.shortcuts import render, redirect, get_object_or_404
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
            product.icon = "images/" + request.POST['icon']
            product.image = "images/" + request.POST['image']
            product.hunter = request.user

            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                product.url = request.POST['url']
            else:
                product.url = "http://{}".format(request.POST['url'])

            product.save()
            return redirect('/products/{}'.format(str(product.id)))
        else:
            return render(request, 'product/create.html', {"error":"All fields are required!"})
    else:
        return render(request, 'product/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, "product/detail.html", {"product":product})
