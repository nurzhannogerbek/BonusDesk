from django import template
from dashboard.models import Payment
from datetime import date


register = template.Library()


@register.filter(name='payment_status')
def payment_status(value):
    payment = Payment.objects.filter(
        user=value,
        date__month=date.today().month,
        date__year=date.today().year,
        paid=True
    ).exists()
    if payment:
        return True
    else:
        return False
