from django.contrib import admin
from .models import User,User_account,User_transaction

# Register your models here.

class User_transactionModelAdmin(admin.ModelAdmin):
    """用户交易表模型管理类"""
    list_display = ['id', "associated_account", "associated_user", "price", "date","status","is_exceed_200"]

# admin.site.register(模型类, 模型管理类)
admin.site.register(User_transaction, User_transactionModelAdmin)

