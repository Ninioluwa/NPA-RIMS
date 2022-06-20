from django.contrib import admin

# Register your models here.
from .models import IssuesModel
from .models import Profile
from .models import Branch
from .models import User

admin.site.register(IssuesModel)
admin.site.register(Profile)
admin.site.register(Branch)
admin.site.register(User)