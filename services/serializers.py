from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField

from api.models import MiningBot


class MiningBotSerializer(ModelSerializer):
    mine_url = HyperlinkedIdentityField(view_name='mine',lookup_field = 'id')
    class Meta:
        model = MiningBot
        fields = (
            'id',
            'name',
            'price',
            'cool_down_time',
            'hp',
            'max_hp',
            'mine_url'
        )