from django.contrib import admin

from .models import Announcement, Comment, FranshizaCafe, Cafe

admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(FranshizaCafe)
admin.site.register(Cafe)
