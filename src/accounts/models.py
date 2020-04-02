from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if email:
            email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    name = models.CharField(_('name'), max_length=120)
    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(
        verbose_name=_(u'Equipe?'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_(u'Ativo?'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_(u'Entrou em'),
        auto_now_add=True
    )

    objects = UserManager()

    class Meta:
        verbose_name = _('cutomer')
        verbose_name_plural = _('customers')

    def __str__(self):
        return self.name
