from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
   
    path('',views.addshow,name="addandshow"),
    path('delete/<int:id>/',views.deletestd,name="deletedata"),
    path('<int:id>/',views.update,name="updatedata"),

]
