from django.contrib import admin
from .models import Message, Secret


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    exclude = []


@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    exclude = []
