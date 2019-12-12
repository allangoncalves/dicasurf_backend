from django.db import models

# Create your models here.

class WhoWeArePage(models.Model):
    
    class Meta:
        verbose_name = "Quem Somos"
        verbose_name_plural = "Quem Somos"
    
    def __str__(self):
        return "Quem Somos"

class PartnerPage(models.Model):

    class Meta:
        verbose_name = "Parceiros"
        verbose_name_plural = "Parceiros"
    
    def __str__(self):
        return "Parceiros"

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

class PartnerSlide(models.Model):
    page = models.ForeignKey(PartnerPage, related_name="carousel", on_delete=models.CASCADE,)
    video_url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Carousel"
    
    def __str__(self):
        return f'{self.id}' 

class WhoWeAreSlide(models.Model):
    page = models.ForeignKey(WhoWeArePage, related_name="carousel", on_delete=models.CASCADE,)
    video_url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Carousel"
    
    def __str__(self):
        return f'{self.id}' 


# Possible to remove
class Slide(models.Model):
    page = models.ForeignKey(HomePage, related_name="carousel", on_delete=models.CASCADE,)
    title = models.CharField("Título", max_length=20)
    text = models.CharField("Texto", max_length=140)
    hashtag = models.CharField("Hastag", max_length=20, blank=True)
    image = models.ForeignKey(Image, related_name="slides", on_delete=models.SET_NULL, verbose_name="Imagem de fundo", null=True)
    
    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Carousel"

