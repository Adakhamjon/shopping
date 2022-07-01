from Store.models import Category,Subcategory,Product
from shopping.models import Cart,CartItem
def categories(request):
	categories = Category.objects.all()
	subcategories = Subcategory.objects.all()
	latest_products = Product.objects.filter(is_active=True).order_by("-updated_at")[:5]
	max_price = Product.objects.filter().order_by("-price").first().price

	session_id = request.session.session_key
	carts = Cart.objects.filter(session_id=session_id)
	if carts.exists():
		cart = carts.first()
	else:
		cart = None

	amount = 0

	if cart:
		cartitems = CartItem.objects.filter(cart = cart)
		for cartitem in cartitems:
			amount += cartitem.quantity
	return {
	"categories":categories,
	"subcategories":subcategories,
	"latest_products":latest_products,
	"max_price": max_price,
	"cartitems_amount":amount
	}