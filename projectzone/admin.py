from django.contrib import admin
from .models import ContectModel
# Register your models here.

@admin.register(ContectModel)
class ContectModelAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']
