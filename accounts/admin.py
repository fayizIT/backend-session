from django.contrib import admin
from .models import CustomUser,AccountInfo

admin.site.register(CustomUser)
admin.site.register(AccountInfo)