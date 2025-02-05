from django.conf.urls import url
from django.urls import path
from food import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('hello/<str:name>', views.hello),
    path('random/', views.random_number),
    path('random/<int:max>/', views.random_number_max),
    path('random/<int:min_>/<int:max_>', views.random_number_mixed),
]