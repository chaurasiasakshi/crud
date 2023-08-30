from django.contrib import admin

# Register your models here.
from .models import crud
@admin.register(crud)

class crudAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','address','age','photo')