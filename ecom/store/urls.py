from django.urls import path,include

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path("SignUp/",views.SignUp,name="SignUp"),
    path("SignUpDone/",views.SignUpDone,name="SignUpDone"),  
	path('cart/', views.cart, name="cart"),
	path('chekout/', views.chekout, name="chekout"),
	path('updateItem/', views.updateItem, name="updateItem"),

]