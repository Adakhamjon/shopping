from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Product,Category,Subcategory
from .utils import *
from django.db.models import Q
from shopping.views import get_cart
from shopping.models import CartItem
from django.contrib.auth.decorators import login_required
# @login_required(login_url="/accounts/login")
def home(request):
	products = Product.objects.filter(is_active=True)
	
	context = {
	"products":products,
	
	}

	return render(request,"index.html",context)
@login_required(login_url="/accounts/login")
def strich_search(items,word):
	return items.filter(title__cointains=word,description__contains=word)

def board_search(items,word):
	return items\
	.filter(Q(title__cointains=word)| Q(description__contains=word))


@login_required(login_url="/accounts/login/")
def store(request):
	page = 1
	if request.GET.get("page",None):
		page = request.GET.get("page",None)

	products = Product.objects.all()
	word = request.GET.get("q",None)
	if word:
		products = strich_search(products,word)

	products = min_max_filter(request,products)
	pages = Paginator(products,3)
	products = pages.get_page(page)
	context = {
	"products": products,
	"pages":pages
	}
	return render(request,"store.html",context)

@login_required(login_url="/accounts/login")
def category_products(request,category_slug):
	page = 1
	if request.GET.get("page",None):
		page = request.GET.get("page",None)

	category = get_object_or_404(Category,slug=category_slug)
	products = Product.objects.filter(sub_category__category = category)
	print(products)
	products = min_max_filter(request,products)
	
	pages = Paginator(products,3)
	products = pages.get_page(page)

	context = {
	"products":products
	}
	return render(request,"store.html",context)


@login_required(login_url="/accounts/login")
def sub_category_products(request,category_slug,sub_category_slug):
	page = 1
	if request.GET.get("page",None):
		page = request.GET.get("page",None)

	category = get_object_or_404(Category,slug=category_slug)
	subcategory = get_object_or_404(Subcategory,slug=sub_category_slug,category =category)
	products = Product.objects.filter(sub_category=subcategory)
	products = min_max_filter(request,products)

	pages = Paginator(products,3)
	products = pages.get_page(page)

	context = {
	"products":products
	}
	return render(request,"store.html",context)

@login_required(login_url="/accounts/login")
def product_details(request,slug):
	products = Product.objects.filter(slug=slug)
	if products.exists():
		product = products.first()

	if request.method == "POST":
		color = request.POST.get("color","")
		size = request.POST.get("size","")
		cart = get_cart(request)

		cartitems = CartItem.objects.filter(cart = cart, product = product)

		if color:
			cartitems = cartitems.filter(color=color)

		if size:
			cartitems = cartitems.filter(size=size)
		if size == "-1" and color == "-1":
			pass
		

		elif cartitems.exists():
			cartitem = cartitems.first()
			cartitem.quantity +=1 
			cartitem.save()

		else:
			cartitem = CartItem(product = product, cart = cart,color=color,size=size)

			cartitem.save()

	context={
	"product":product
	}
	return render(request,"product_details.html",context)
