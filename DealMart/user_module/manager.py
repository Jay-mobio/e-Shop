"""USER MANAGER"""
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """USERR MANAGER"""
    use_in_migrations = True
    def create_user(self,email,password=None,**extra_fields):
        """CREATE USER"""
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        """"CREATE SUPERUSER"""
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have id_staff true'))
        return self.create_user(email,password,**extra_fields)
