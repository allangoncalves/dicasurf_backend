from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


SEX = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
)

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField("Nome", max_length=50)
    nickname = models.CharField("Apelido", max_length=50)
    country = models.CharField("País", max_length=50)
    state = models.CharField("Estado", max_length=50)
    city = models.CharField("Cidade", max_length=50)
    address = models.CharField("Localidade", max_length=255)
    sex = models.CharField("Sexo", max_length=30, choices=SEX)
    news = models.BooleanField("Receber notícias", default=False)
    terms = models.BooleanField(default=True)