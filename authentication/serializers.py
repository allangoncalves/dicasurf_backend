from authentication.models import User, UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def validate_terms(self, value):
        if not value:
            raise serializers.ValidationError("Você não aceitou os termos.")
        return value

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.name = profile_data.get('name', profile.name)
        profile.nickname = profile_data.get('nickname', profile.nickname)
        profile.country = profile_data.get('country', profile.country)
        profile.state = profile_data.get('state', profile.state)
        profile.city = profile_data.get('city', profile.city)
        profile.address = profile_data.get('address', profile.address)
        profile.sex = profile_data.get('sex', profile.sex)
        profile.save()

        return instance