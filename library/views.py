from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Author


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class AuthorsView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = "library/author_list.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "library/author_detail.html"
    context_object_name = 'author'
