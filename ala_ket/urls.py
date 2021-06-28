from django.contrib import admin
from django.urls import path, include

from users.views import ProfileRegisterView, StuffLoginView, StuffRegisterView, ProfileLoginView

from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
    path('stuff/register', StuffRegisterView.as_view()),
    path('stuff/login', StuffLoginView.as_view()),
    path('cafe/', include('cafes.urls')),
]