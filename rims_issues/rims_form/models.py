from django.db import models
from django.contrib.auth.models import AbstractUser


# many issues to a port

class User(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Branch(models.Model):
     # Port Choices
    CHOICES = [
        ('LAGOS', 'Lagos'),
        ('TIN-CAN', 'Tin-Can'),
        ('RIVERS', 'Rivers'),
        ('DELTA', 'Delta'),
        ('CALABAR', 'Calabar'),
        ('ONNE', 'Onne')
    ]
    port =  models.CharField(max_length = 10, choices = CHOICES)

    def __str__(self):
        return self.get_port_display()




class IssuesModel(models.Model):

    port = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sen_no = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 100)
    issues = models.TextField()
    date_submitted = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.subject


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access = models.BooleanField(default = False)
    port = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

