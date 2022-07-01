from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name="list"),
    path("update/<int:pk>/",update,name="update"),
    path("create/",create, name="create"),
    path("delete/<int:pk>/",delete_book,name = "delete-book"),
    path("example/",category_example_form,name="category-form")
    
]