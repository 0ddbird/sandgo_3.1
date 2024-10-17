from django.contrib import admin

from app_1.models import ModelOne


# Register your models here.
@admin.register(ModelOne)
class ModelOneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
    )
