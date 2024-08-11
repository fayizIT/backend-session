from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        normalized_email=self.normalize_email(email)
        email_org=normalized_email.lower()

        user = self.model(email=email_org,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None,**extra_fields):
        user = self.create_user(email,password=password,**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser):
    Role_Choices = [
      ("collector","Collector"),
      ("user","User"),
      ("staff","Staff")
      ("superser","SuperUser")
    ]
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20,choices=Role_Choices, default= "user")
    otp = models.CharField(max_length=6, blank=True, null=True) 
    is_active = models.BooleanField(default=True)
    is_collector = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.role = "admin"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True
    
class AccountInfo(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE , related_name="account_info")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin_code = models.IntegerField()
    latitude =models.DecimalField(max_digits=30, decimal_places=20,default=None)
    longitude =models.DecimalField(max_digits=30, decimal_places=20,default=None)

    def __str__(self):
        return  f"{self.user} {self.latitude}{self.longitude}"
