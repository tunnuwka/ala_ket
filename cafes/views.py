from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response

from .models import Cafe, Comment, Announcement, FranshizaCafe 
from .serializers import CafeSerializer, CommentSerializer,AnnouncementSerializer, FranshizaCafeSerializer
from .permissions import IsAdminUserClubCreate, IsAdminOrCreateClub

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CafeView(ModelViewSet):
    queryset = Cafe.objects.prefetch_related('announcement_cafe')
    serializer_class = CafeSerializer 
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class AnnouncementView(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminOrCreateClub, )

class FranshizaCafeView(ModelViewSet):
    queryset = FranshizaCafe.objects.all()
    serializer_class = FranshizaCafeSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminOrCreateClub, )

class CommentView(ModelViewSet):
    queryset = Comment.objects.prefetch_related('announcements_comments')
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated, )