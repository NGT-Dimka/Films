from venv import create

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password, check_password, PBKDF2PasswordHasher


class PasswordHash(PBKDF2PasswordHasher):
    algorithm = 'pbkdf2_wrapped_sha1'

    def encoded(self, sha1_hash, salt):
        return super(PasswordHash, self).encode(sha1_hash, salt)


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        else:
            username = self.model(username=username)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            token = make_password(password, salt=PasswordHash, hasher='default')
            if check_password(password, PasswordHash.encoded) is not True:
                ValueError('Password is not correct')
            else:
                user = self.model(is_active=True, is_superuser=True)
                user = user.save(username=username, password=token)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        else:
            return self._create_user(username, password, **extra_fields)
