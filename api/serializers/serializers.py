from custom_auth.models import CustomUser
from rest_framework.serializers import ModelSerializer,SerializerMethodField,CharField
from custom_auth.validators import validate_username

class UserSerializer(ModelSerializer):
    username = CharField(validators = [validate_username])
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "state_of_origin",
            "state_of_residence"
        ]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("id","password")