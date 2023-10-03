from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addTicket),
    path('delete/<int:ticket_id>/', views.deleteTicket, name='delete_ticket'),
    path('update_status/<int:ticket_id>/', views.updateStatus, name='update_status'),
]
