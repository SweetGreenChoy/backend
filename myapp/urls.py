from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    #path('', views.ticket_index, name='ticket_index'),
	path('reserve/<seat>/', views.ticket_reserve, name='reserve'),
]