from django.contrib import admin
from .models import Photo
from .models import User

# Register your models here.
admin.site.register(Photo)
admin.site.register(User)
