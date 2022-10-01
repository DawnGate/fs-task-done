from rest_framework import serializers

from .models import SignUpEmail

class SignUpEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpEmail
        fields = ['email', 'add_date']