from rest_framework.serializers import ModelSerializer,SerializerMethodField,CharField,BaseSerializer

from api.models import Wallet

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"