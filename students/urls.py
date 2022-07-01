from django.urls import path
from .views import *

urlpatterns = [
   path("",index,name ="student-list"),
   path("create/",create,name = "add-student"),
   path("update/<int:pk>/",update,name = "update-student"),
   path("delete/<int:pk>/",delete,name = "delete-student")

]