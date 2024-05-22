from django.urls import path
from . import views

urlpatterns = [
  path('', views.register),
  path('all/', views.list),
  path('del/<id>', views.delete),
  path('upd/<id>', views.update),
]