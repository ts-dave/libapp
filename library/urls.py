from django.urls import path
from .views import HomeView, AuthorsView, AuthorDetailView

app_name = "library"
urlpatterns = [
    path("", HomeView.as_view(), name='dashboard'),
    path("authors", AuthorsView.as_view(), name="authors"),
    path("author/<int:pk>", AuthorDetailView.as_view(),
         name="author_detail"),
]
