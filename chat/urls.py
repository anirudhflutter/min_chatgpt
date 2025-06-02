from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    path('ask/', views.ask_gpt, name='ask_gpt'),
]
