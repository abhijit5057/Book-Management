from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from app_demo.models import Author
from django.dispatch import receiver

@receiver(post_save, sender=Author)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='user_permission'))

    post_save.connect(create_user_profile, sender=Author)

    