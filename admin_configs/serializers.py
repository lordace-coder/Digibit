from rest_framework.serializers import ModelSerializer,SerializerMethodField,CharField,BaseSerializer,HyperlinkedIdentityField
from api.models import MiningBot




class CreateBotSerializer(ModelSerializer):
    class Meta:
        model = MiningBot
        exclude = ('id',)