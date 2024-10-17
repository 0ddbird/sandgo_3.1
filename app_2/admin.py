from django.contrib import admin

from app_2.models import ModelTwo


# Register your models here.
@admin.register(ModelTwo)
class ModelTwoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
    )
