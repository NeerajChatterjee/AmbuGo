from rest_framework import serializers
from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        fields = ('id', 'phone', 'first_name',
                  'last_name', 'gender', 'date_of_birth', 'is_onboarded')
