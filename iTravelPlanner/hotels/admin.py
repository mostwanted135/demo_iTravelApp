from django.contrib import admin
from .models import ApiReturnList,PnrConfirmedList

# Register your models here.

admin.site.register(ApiReturnList)
admin.site.register(PnrConfirmedList)

