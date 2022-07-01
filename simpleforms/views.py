from django.shortcuts import render,resolve_url,redirect
from django.urls import reverse
from .models import Books,Genre,Filial,Director
from .forms import BooksForm
from .utils import get_parse_time

def index(request):
	filials = Filial.objects.all()
	# books = Books.objects.all()
	context = {
	"filials":filials
	# "books":books

	}
	return render(request,"simpleforms/list.html",context)



def create(request):
	if request.method == "POST":
		title = request.POST.get("title",None)
		date = request.POST.get("date",None)
		time = request.POST.get("time",None)
		director = request.POST.get("director",None)
		experience = request.POST.get("experience",None)
		# with transaction.atomic():
		f = Filial(title=title,
			established_at=get_parse_time(date,time))
		f.save()

		d = Director(fullname=director,experience=experience,filial=f)
		d.save()
		return redirect(reverse("list"))



	# form = BooksForm()
	# if request.method=="POST":
	# 	form = BooksForm(request.POST,request.FILES)
	# 	if form.is_valid():
	# 		form.save()
			# book = BooksForm()
			# book.title = form.cleaned_data["title"]
			# book.author = form.cleaned_data["author"]
			# book.genre = form.cleaned_data["genre"]
			# book.image = form.cleaned_data["image"]
			# book.year = form.cleaned_data["year"]
			# book.save()

			# return redirect(reverse("list"))

	# 	title = request.POST.get("title",None)
	# 	author = request.POST.get("author",None)
	# 	genre_id = request.POST.get("genre_id",None)
	# 	year = request.POST.get("year",None)

	# 	genre = Genre.objects.get(id=genre_id)

	# 	book = Books()
	# 	book.title = title
	# 	book.author = author
	# 	book.genre = genre
	# 	book.year = year
	# 	book.save()

		# return redirect(reverse("list"))

	# genres = Genre.objects.all()
	# context = {

	# # "form":form
	# # "genres":genres
	# }
	return render(request,"simpleforms/create.html")

def update(request,pk):
	try:
		filial = Filial.objects.get(id=pk)
		date = filial.established_at.strftime("%Y-%m-%d")
		time = filial.established_at.strftime("%H:%M")
	except:
		return redirect(reverse("list"))
	if request.method == "POST":
		title = request.POST.get("title",None)
		date = request.POST.get("date",None)
		time = request.POST.get("time",None)
		director = request.POST.get("director",None)
		experience = request.POST.get("experience",None)
		

		# with transaction.atomic():
		filial.title=title
		filial.established_at = get_parse_time(date,time)
		filial.director.fullname = director
		filial.director.experience = experience
		print(filial.director.experience)
		filial.save()
		# d = Director(fullname=director.,experience=experience,filial=filial)
		# d.save()
		return redirect(reverse("list"))
	# books = Books.objects.filter(id=pk)
	# if not books.exists():
	# 	return redirect(reverse("list"))
	# else:
	# 	books=books.first()

	# form = BooksForm(instance=books)


	# if request.method=="POST":
	# 	books = BooksForm(request.POST,request.FILES,instance=books)
	# 	if books.is_valid():
	# 		books.save()
	# 		return redirect(reverse("list"))


		# title = request.POST.get("title",None)
		# author = request.POST.get("author",None)
		# genre_id = request.POST.get("genre_id",None)
		# year = request.POST.get("year",None)

		# genre = Genre.objects.get(id = genre_id)

		# books.title = title
		# books.author = author
		# books.genre= genre
		# books.year = year
		# book.image = form.cleaned_data["image"]
		# books.save()
	# genres = Genre.objects.all()
	context = {
	"filial":filial,
	"date":date,
	"time":time,


	# "form":form
	# "genres":genres,
	# "books":books
	}
	return render(request,"simpleforms/update.html",context)


def delete_book(request,pk):
	try:
		filial = Filial.objects.get(id=pk)
		filial.delete()
	except Filial.DoesNotExist:
		pass
	# try:
	# 	books = Books.objects.get(id = pk)
	# 	books.delete()
	# except Books.DoesNotExist:
	# 	pass

	return redirect(reverse("list"))

def category_example_form(request):
	form = CategoryForm()
	context={
	"form":form
	}
	return render(request,"simpleforms/example.html",context)
