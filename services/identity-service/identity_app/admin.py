from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domain', 'parent')
    search_fields = ('name', 'domain')