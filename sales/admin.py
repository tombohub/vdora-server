from django.contrib import admin
from .models import Sale, NooksPayoutSchedule


class SaleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sale._meta.fields]


admin.site.register(Sale, SaleAdmin)
admin.site.register(NooksPayoutSchedule)
