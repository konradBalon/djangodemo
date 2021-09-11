from django.conf.urls import url
from django.urls import path
from food import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('random/', views.random_number),
    path('random/<int:max>/', views.random_number_max),
]