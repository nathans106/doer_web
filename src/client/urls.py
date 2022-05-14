from django.urls import path

from . import views

urlpatterns = [
    path('', views.today, name='today'),
    path('<int:year>/<int:month>/<int:day>/', views.day, name='day')
]
