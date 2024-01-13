from django.contrib import admin
from .models import (Category, Author, Book, MemberStatus,
                     Member, ReservationStatus, Reservation, Loan,
                     LoanStatus)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'year', 'pages', 'copies_owned']


@admin.register(MemberStatus)
class MemberStatusAdmin(admin.ModelAdmin):
    list_display = ["status"]


@admin.register(LoanStatus)
class LoanStatusAdmin(admin.ModelAdmin):
    list_display = ["status"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'joined_date', 'active_status']


@admin.register(ReservationStatus)
class ReservationStatusAdmin(admin.ModelAdmin):
    list_display = ['status']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'reservation_status']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'loan_date', 'loan_status',
                    'returned_date']
