from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Хэшируем пароль перед сохранением модели
        obj.password = make_password(obj.password)
        obj.save()


admin.site.register(CustomUser, CustomUserAdmin)
