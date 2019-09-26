from django.db import models

# Create your models here.

class HomePage(models.Model):
    class Meta:
        verbose_name = "Página Inicial"
        verbose_name_plural = "Página Inicial"
    
    def __str__(self):
        return "Página Inicial"

class Slide(models.Model):
    page = models.ForeignKey(HomePage, related_name="carousel", on_delete=models.CASCADE,)
    title = models.CharField("Título", max_length=20)
    text = models.CharField("Texto", max_length=140)
    hashtag = models.CharField("Hastag", max_length=20, blank=True)
    image = models.ImageField("Imagem de fundo")
    
    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Carousel"
