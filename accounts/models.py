# from django.db import models

# from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _


# class User(AbstractUser):
#     class Types(models.TextChoices):
#         CUSTOMER = "CUSTOMER", "Customer"
#         OWNER = "OWNER", "Owner"

#     base_type = Types.Customer

#     type = models.CharField(
#         _("Type"), max_length=50, choices=Types.choices, default=base_type
#     )


#     name = models.CharField(_("Name of User"), blank=True, max_length=255)

#     def get_absolute_url(self):
#         return reverse("users:detail", kwargs={"username": self.username})

class Customer(User):

    class Meta:
        proxy = True

class Owner(User):

    class Meta:
        proxy = True