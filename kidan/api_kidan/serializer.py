from rest_framework import serializers
from .models import Account, Kids

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'tag', 'bio', 'email', 'date_of_birth', 'joined_at')

