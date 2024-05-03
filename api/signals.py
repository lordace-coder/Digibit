from ace_tokens.models import PasswordTokens as Tokens
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender = Tokens)
def handle_token_created(sender,instance:Tokens,created,*args, **kwargs):

    if created:
        # todo send email to user here
        raise Exception("Email functionality hasnt been implemented yet")