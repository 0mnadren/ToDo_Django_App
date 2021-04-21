from django.contrib import admin
from .models import (
    Profile,
    Todo,
    Notes,
)

admin.site.register(Profile)
admin.site.register(Todo)
admin.site.register(Notes)
