from django.db import models

from . import user_models

__all__ = ['Staff']


class Staff(models.Model):
    """
    This model stores all staff's email addresses. When user register account, it will check if user's email address
    in this table. If yes, they're staff, otherwise they are regular users
    """
    email = models.EmailField(max_length=50, null=False)
