import json
import random
from faker import Faker
from library.models import Author, Book, Category

fake = Faker()

with open("books.json", "r") as f:
    data = json.load(f)

for book in data:
    categories = ["Fantasy", "Adventure", "Romance", "Contemporary", "Dystopian",
                  "Mystery", "Horror", "Thriller", "Paranormal",
                  "Historical fiction", "Science Fiction", "Cookbook",
                  "Personal Development", "Motivational", "Health",
                  "History", "Humor"]
    category = random.choice(categories)
    category = Category.objects.get(name=category)
    authors = Author.objects.filter(last_name=book["author"].split()[-1])
    title = book["title"]
    language = book["language"]
    year = book["year"]
    pages = book["pages"]
    link = book["link"]
    if not link:
        link = fake.url()
    book = Book.objects.create(title=title, category=category,
                               language=language, year=year,
                               pages=pages, link=link)
    for author in authors:
        book.authors.add(author.id)

# *first_name, last_name = book["author"].split()
    # first_name = ' '.join(first_name)
    # if not first_name:
    #     first_name = fake.first_name()
    # if last_name == 'Unknown':
    #     last_name = fake.last_name()
    # country = book["country"]
    # author = Author.objects.get_or_create(first_name=first_name,
    #                                last_name=last_name,
    #                                country=country)
    # print("Done with author!!!")