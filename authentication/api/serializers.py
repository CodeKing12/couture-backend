from rest_framework.serializers import ModelSerializer
from authentication.models import Account

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        # I excluded both info because drf tries to manually populate them during user creation which throws a Direct Assignment error.
        # If you want to include both groups and user_permissions in the returned serialized data, you can create a RegistrationSerializer that excludes them during user creation and then remove them from the exclude list in this AccountSerializer.
        exclude = ['groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'write_only': True},
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)