from cafes.models import FranshizaCafe
from django.urls import path, include

from .views import CafeView, AnnouncementView, FranshizaCafeView, CommentView






urlpatterns = [
    path('cafe/', CafeView.as_view({'get': 'list', 'post': 'create'})),
    path('cafe/<int:pk>/', CafeView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
    path('announcement/', AnnouncementView.as_view({'get': 'list', 'post': 'create'})),
    path('announcement/<int:pk>', AnnouncementView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
    path('franshizacafe/', CafeView.as_view({'get': 'list', 'post': 'create'})),
    path('franshizacafe/<int:pk>', FranshizaCafeView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
    path('comment/', CommentView.as_view({'get': 'list', 'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}))
]