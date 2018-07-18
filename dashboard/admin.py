from django.contrib import admin
from dashboard.models import (
    Payment,
    Profile,
)


class PaymentAdmin(admin.ModelAdmin):
    search_fields = (
        'user__username',
        'user__email',
    )
    list_filter = (
        'paid',
        'date',
    )


admin.site.register(Payment, PaymentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    search_fields = (
        'user__username',
        'user__email',
    )


admin.site.register(Profile, ProfileAdmin)
