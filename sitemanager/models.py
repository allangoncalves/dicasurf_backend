from django.db import models

# Create your models here.

class HomePage(models.Model):
    class Meta:
        verbose_name = "Página Inicial"
        verbose_name_plural = "Página Inicial"
    
    def __str__(self):
        return "Página Inicial"

class Image(models.Model):
    title = models.CharField("Título", max_length=30, unique=True)
    image = models.ImageField("Imagem")

    def __str__(self):
        return f'{self.title}'


class Slide(models.Model):
    page = models.ForeignKey(HomePage, related_name="carousel", on_delete=models.CASCADE,)
    title = models.CharField("Título", max_length=20)
    text = models.CharField("Texto", max_length=140)
    hashtag = models.CharField("Hastag", max_length=20, blank=True)
    image = models.ForeignKey(Image, related_name="slides", on_delete=models.PROTECT, verbose_name="Imagem de fundo",)
    
    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Carousel"

