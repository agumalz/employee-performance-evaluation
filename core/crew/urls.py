from django.urls import path
from . import views

urlpatterns = [
    path('', views.crew_main, name='crew_main'),
    path('crew_create', views.crew_create, name='crew_create'),
    path('edit/<int:id>/', views.crew_edit, name='crew_edit'),
    path('delete/<int:id>/', views.crew_delete, name='delete')
]
