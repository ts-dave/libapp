from django.db import models

# TODO: Add notifications and messages
# TODO: Notifications are for all
# TODO: Messages are perculiar to each user


class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    about = models.TextField(blank=True, null=True)
    headshot = models.ImageField(upload_to="static/images",
                                 null=True, blank=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.ManyToManyField(Author, related_name='books',
                                     db_table='book_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='books')
    synopsis = models.TextField(blank=True, null=True)
    volume = models.IntegerField(default=1)
    language = models.CharField(max_length=120)
    year = models.CharField(max_length=4)
    copies_owned = models.IntegerField(default=0)
    pages = models.IntegerField()
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}, ({self.copies_owned})"


class MemberStatus(models.Model):
    status = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Member status"

    def __str__(self):
        return self.status


class Member(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    joined_date = models.DateTimeField(auto_now=True)
    active_status = models.ForeignKey(MemberStatus, on_delete=models.CASCADE,
                                      related_name="members")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class ReservationStatus(models.Model):
    status = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Reservation status"

    def __str__(self):
        return self.status


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='reservations')
    member = models.ForeignKey(Member, on_delete=models.CASCADE,
                               related_name='reservations')
    reservation_date = models.DateTimeField(auto_now=True)
    reservation_status = models.ForeignKey(ReservationStatus,
                                           on_delete=models.CASCADE,
                                           related_name='reservations')

    def __str__(self):
        return f"{self.book} - {self.member}"


class LoanStatus(models.Model):
    status = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Loan status"

    def __str__(self):
        return self.status


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name="loans")
    member = models.ForeignKey(Member, on_delete=models.CASCADE,
                               related_name="loans")
    loan_date = models.DateTimeField(auto_now=True)
    loan_status = models.ForeignKey(LoanStatus, on_delete=models.CASCADE,
                                    related_name='loans')
    returned_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.book} - {self.member}"
