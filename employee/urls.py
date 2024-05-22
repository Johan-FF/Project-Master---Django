from django.urls import path
from . import views

urlpatterns = [
  path('', views.create),
  path('all/', views.list),
  path('del/<id>', views.delete),
  path('upd/<id>', views.update),
  path('by-organization/<id>', views.by_organization),
]