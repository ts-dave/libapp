from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - Last login: {self.last_login}"
