from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


# Gerenciador do Usuário
class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('O Username é obrigatório')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    empresa = models.CharField('Empresa', max_length=100)
    is_staff = models.BooleanField('Membro da equipe', default=False)
    is_adm = models.BooleanField('Usuário Administrativo', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['empresa']

    def __str__(self):
        return f'{self.empresa} {self.username}'

    objects = UsuarioManager()
