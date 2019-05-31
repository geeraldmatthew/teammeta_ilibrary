from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from .models import Book

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        
        data["message"] = "Hello asdhasdas"
        return data 

class BookListView(ListView):
	template_name = "book-list.html"
	model = Book

class BookDetailView(DetailView):
	
	model = Book