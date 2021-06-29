
from rest_framework import serializers
from .models import FranshizaCafe, Cafe, Announcement, Comment


class CafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    announcements_comments = CommentSerializer(many=True, read_only=True)
    announcement_cafe = CafeSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ('id', 'news', 'text', 'image', 'cafe', 'date', 'announcement_cafe', 'announcements_comments')


class FranshizaCafeSerializer(serializers.ModelSerializer):
    cafe = CafeSerializer(many=True, read_only=True)

    class Meta:
        model = FranshizaCafe
        fields = ('id', 'cafe', 'cafe')
