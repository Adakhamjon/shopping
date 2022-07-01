from django import forms
from .models import Genre,Books
# class CategoryForm(forms.Form):
# 	name = forms.CharField(label="Ism")

# class BooksForm(forms.Form):
	# title = forms.CharField(max_length=255)
	# author = forms.CharField()
	# genre = forms.ModelChoiceField(
	# 	queryset=Genre.objects.all())
	# year = forms.CharField()
	# image = forms.ImageField()



class BooksForm(forms.ModelForm):
	class Meta:
		model = Books
		fields = "__all__"


	def __init__(self,*args,**kwargs):
		super(BooksForm,self).__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs["class"] = "form-control"