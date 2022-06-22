from django.contrib import admin

# Register your models here.
from .models import IssuesModel
from .models import User

admin.site.register(IssuesModel)
admin.site.register(User)
