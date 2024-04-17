from django.db import models

from user_module.models import CustomUser

# Create your models here.
class Newsletter(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="کاربر")
    email = models.EmailField(verbose_name="ایمیل", unique=True)


    def __str__(self):
        return f'{self.user.username} - {self.email}'
    
    class Meta:
        verbose_name = "خبرنامه"
        verbose_name_plural = "خبرنامه ها"