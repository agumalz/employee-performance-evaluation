from django.urls import path
from . import views
from .views import dashboard_chart_data

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/chart-data/', dashboard_chart_data, name='dashboard_chart_data'),
]