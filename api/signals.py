from ace_tokens.models import PasswordTokens as Tokens
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from custom_auth.models import CustomUser
from .models import Profile

@receiver(post_save,sender = Tokens)
def handle_token_created(sender,instance:Tokens,created,*args, **kwargs):
    if created:
        # todo send email to user here
        raise Exception("Email functionality hasnt been implemented yet")


@receiver(post_save,sender = CustomUser)
def create_users_profile(sender,instance:CustomUser,created,*args, **kwargs):
    #* check if the instance was just created or if it has existed since but user still doesnt have a profile
    qs = Profile.objects.filter(user = instance)
    if created or not qs.exists():
        Profile.objects.create(user = instance)