from django.contrib import admin

from accounts.models import User, SetToken, BlackListEmail

admin.site.register(User)
admin.site.register(SetToken)
admin.site.register(BlackListEmail)
