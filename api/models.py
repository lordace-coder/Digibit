from typing import Iterable
from django.db import models
from custom_auth.models import CustomUser
from cloudinary.models import CloudinaryField
from ace_tokens.generate_token import generate_token
from decimal import Decimal

class MiningBot(models.Model):
    id = models.CharField(max_length=22,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    cool_down_time = models.IntegerField()
    hp = models.DecimalField(decimal_places=2,max_digits=10)
    max_hp = models.DecimalField(decimal_places=2,max_digits=10,default=100)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def is_active(self):
        return self.hp> 0.0
    
    def save(self, *args,**kwargs) -> None:
        id = f"0x{generate_token(20)}"
        id_already_exists = MiningBot.objects.filter(id = id).exists()
        # *loop till we generate an unexisting id
        while id_already_exists:
            id = f"0x{generate_token(20)}"
            id_already_exists = MiningBot.objects.filter(id = id).exists()
            if not id_already_exists:
                break
        self.id = id
        return super().save(*args,**kwargs)

    def clone_bot(self):
        clone = MiningBot.objects.create(
                                            name=self.name,
                                            cool_down_time = self.cool_down_time,
                                            price = self.price,
                                            hp = self.max_hp,
                                            max_hp = self.max_hp
                                        )
        return clone


class Wallet(models.Model):
    """
        REMEMBER TO CREATE WALLET USING THE create_wallet STATIC METHOD
    """
    address = models.CharField(max_length=22,primary_key=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cryptonites = models.DecimalField(default=0.0,decimal_places=4,max_digits=7)
    crypton = models.DecimalField(default=0.0,decimal_places=2,max_digits=7)

    @staticmethod
    def create_wallet(user:CustomUser):
        # todo generate wallet address here
        address = f"0x{generate_token(20)}"
        address_already_exists = Wallet.objects.filter(address = address).exists()
        # *loop till we generate an unexisting address
        while address_already_exists:
            address = f"0x{generate_token(20)}"
            address_already_exists = Wallet.objects.filter(address = address).exists()
            if not address_already_exists:
                break
    
        new_wallet = Wallet(address = address,owner = user)
        new_wallet.save()
        return new_wallet
    
    def __str__(self) -> str:
        return f"{self.owner.username}'s wallet"

    def send_to_address(self,amt:float,destination):
        # todo send notification to recieving user and sending user about the status of the transaction
        if self.crypton >= amt:
            # *get wallet destination
            reciever = Wallet.objects.filter(address = destination)
            if not reciever.exists():
                raise Exception("Invalid wallet address")
            reciever = reciever[0]
            if reciever.owner.is_verified_user:
                self.crypton -= amt
                reciever.crypton += amt
                # * SAVE NEW BALANCES (probably a good place to send notification)
                self.save()
                reciever.save()
            else:
                raise Exception("Cant send crypton to unverified user")


    def send_to_email(self,amt:float,email):
        # todo send notification to recieving user and sending user about the status of the transaction
        if self.crypton >= amt:
            # *get wallet email
            reciever = Wallet.objects.filter(owner__email = email)
            if not reciever.exists():
                raise Exception("Invalid wallet email")
            reciever = reciever[0]
            if reciever.owner.is_verified_user:
                self.crypton -= amt
                reciever.crypton += amt
                # * SAVE NEW BALANCES (probably a good place to send notification)
                self.save()
                reciever.save()
            else:
                raise Exception("Cant send crypton to unverified user")

    def credit(self,amt:float):
        amt = Decimal(amt)
        self.cryptonites += amt
        self.save()


class Profile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    no_of_referred_users = models.IntegerField(default=0)
    is_vendor = models.BooleanField(default=False)
    bio = models.TextField(max_length=400,null=True,blank=True)
    contact_link = models.URLField(null=True,blank=True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True,blank=True)
    image = CloudinaryField(null=True,blank=True)
    bots = models.ManyToManyField(MiningBot,blank=True,related_name='owned_bot')

    def __str__(self) -> str:
        return self.user.username + " profile"
    
    def save(self, *args,**kwargs) -> None:
        if self.wallet == None:
            self.wallet = Wallet.create_wallet(self.user)
        return super().save(*args,**kwargs)