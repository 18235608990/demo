from django.db import models

# Create your models here.

# 第一题
class User(models.Model):
    # 用户表
    id = models.AutoField(primary_key=True,verbose_name='用户id')
    user = models.CharField(max_length=64,null=True,blank=True,verbose_name='用户名')
    user_email = models.CharField(max_length=64,default=True,verbose_name='用户邮箱')
    user_mobile = models.IntegerField(unique=True,verbose_name='用户手机号')
    u_a = models.ForeignKey('User_account', on_delete=models.CASCADE)


class User_account(models.Model):
    # 用户账户表
    account_number = models.IntegerField(verbose_name='账号')
    balance = models.DecimalField(max_digits=16,decimal_places=2,verbose_name='余额')
    account = models.ForeignKey("User", on_delete=models.CASCADE)


class User_transaction(models.Model):
    # 用户交易表
    status_choices = (
        (0,'交易中'),
        (1,'交易成功'),
        (2,'交易失败'),
    )
    associated_account = models.ForeignKey('User_account',verbose_name='关联账户',on_delete=models.CASCADE)
    associated_user = models.ForeignKey('User',verbose_name='关联用户',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=16,decimal_places=2,verbose_name='交易金额')
    date = models.DateField(verbose_name='交易日期')
    status = models.IntegerField(choices=status_choices, default=1,verbose_name='交易状态')

    # 第四题
    def is_exceed_200(self):
        if self.price > 200:
            return "%s RMB %s" % (self.price, "YES")
        else:
            return "%s RMB %s" % (self.price, "NO")
