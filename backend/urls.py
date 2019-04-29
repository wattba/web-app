from django.urls import path

from . import views

urlpatterns = [
	# path('', views.UserDetail.as_view()),
	path('<slug:pk>/', views.UserDetail.as_view())
]
