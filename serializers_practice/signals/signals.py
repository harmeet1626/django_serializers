# code
from django.db.models.signals import post_save, pre_delete, post_init
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		print('Created object called!')
		# Profile.objects.create(user=instance)
		# Profile.objects.create(user=1,phone = 8628864762)
		pass

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
		# instance.profile.save()
		print("Object saved called")
		pass
