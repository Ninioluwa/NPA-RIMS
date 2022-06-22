from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


# many issues to a port
class CustomManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    CHOICES = [
        ('LAGOS', 'Lagos'),
        ('TIN-CAN', 'Tin-Can'),
        ('RIVERS', 'Rivers'),
        ('DELTA', 'Delta'),
        ('CALABAR', 'Calabar'),
        ('ONNE', 'Onne')
    ]
    port = models.CharField(max_length=10, choices=CHOICES)
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    REQUIRED_FIELDS = ["email", "port"]
    objects = CustomManager()

    def __str__(self):
        return self.email


class IssuesModel(models.Model):
    CHOICES = [
        ('NEW', 'New'),
        ('RESOLVED', 'Resolved')
     ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sen_no = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=CHOICES)
    subject = models.CharField(max_length=100)
    issues = models.TextField()
    date_submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject
