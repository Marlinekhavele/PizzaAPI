
from django.contrib.auth.models import User

class Customer(User):

    class Meta:
        proxy = True

class Staff(User):

    class Meta:
        proxy = True