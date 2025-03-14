from django.urls import path, re_path
from book import views 

urlpatterns = [
    path('add_book/', views.add_book),
    path('show_books/', views.show_books),
    ]