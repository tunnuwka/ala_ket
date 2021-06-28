from django.contrib.auth import get_user_model

from rest_auth.models import TokenModel

from rest_framework import serializers

from users.models import Profile, Stuff


class ProfileRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Profile.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone=validated_data.get('phone'),
        )
        return profile


class StuffRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Stuff.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        return profile



class ProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class StuffLoginSerializer(ProfileLoginSerializer):
    pass


