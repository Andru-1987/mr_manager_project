from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from .models import AigasraUser  # Replace with your custom user model

@receiver(user_logged_in, sender=AigasraUser)
def update_last_login(sender, user, request, **kwargs):
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])