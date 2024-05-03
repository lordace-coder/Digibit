from datetime import datetime, timedelta
from django.db import models
from custom_auth.models import CustomUser
from .generate_token import generate_token


user_model = CustomUser

# Create your models here.
class PasswordTokens(models.Model):
    """
        Creates tokens to be used for password recovery,tokens expire in four minutes
    """
    token = models.CharField(max_length=10,blank = True,null = True)
    user = models.ForeignKey(user_model,on_delete=models.CASCADE)
    expiry = models.DateTimeField(blank = True,null = True)
    created_at = models.DateTimeField(auto_created=True,auto_now=True)

    class Meta:
        verbose_name = "PasswordToken"
        verbose_name_plural = "PasswordTokens"
        
    @staticmethod
    def clear_expired_tokens():
        try:
            current_time = datetime.now()
            qs = PasswordTokens.objects.all()
            for item in qs:
                if current_time >= item.expiry:
                    item.delete()
        except:
            ...
    
    @staticmethod
    def validate_user_token(user:user_model,token:str)->bool:
        """
        checks if token is valid
        """
        try:
            qs = PasswordTokens.objects.get(user = user,token = token)
            qs.delete()
            return True
        except:
            return False    

    
    def save(self, *args, **kwargs) -> None:
        # make sure user has an email address
        if not self.user.email:
            raise Exception('Error: users email cannot be null or /',self.user.email,'/')
        # delete past token instances that belong to this user
        
        old_tokens = PasswordTokens.objects.filter(user = self.user)
        if old_tokens.exists():
            for token_instance in old_tokens:
                token_instance.delete()
                
        if not self.expiry:
            self.expiry = datetime.now()+ timedelta(minutes=4)
            self.token = generate_token(8)
            
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.user.email
    
