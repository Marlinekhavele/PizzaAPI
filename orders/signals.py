from django.contrib.auth.models import User
from accounts.models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import order


@receiver(post_save, sender=User)
def create_customer_order(sender, instance, created, **kwargs):
    if created:
        Order.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer_order(sender, instance, **kwargs):
    instance.order.save()