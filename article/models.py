from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name = "Yazar")
    title = models.CharField(max_length=50, verbose_name = "Konu")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True, null = True, verbose_name= "Makaleye foto ekleyin")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Makale", related_name = "comments")
    comment_author = models.CharField(max_length=50, verbose_name= "İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

class newborn_tpn(models.Model):
    kilo = models.FloatField(verbose_name="Kilo (kg)")
    hafta = models.IntegerField(verbose_name="Hafta (gh)")
    total = models.IntegerField(verbose_name="Total  cc/kg")
    aminoasit = models.FloatField(verbose_name="Aminoasit (gr)")
    sodyum = models.FloatField(verbose_name="Sodyum (meq)")
    potasyum = models.FloatField(verbose_name="Potasyum (meq)")
    kalsiyum = models.FloatField(verbose_name="Calsiyum (meq)")
    glukoz = models.FloatField(verbose_name="Glukoz (gr)")
    lipit = models.FloatField(verbose_name="Lipit (gr)")
    matur = "matur"
    prematur = "pm"
    maturite_secenek = [(prematur, "prematur"),(matur,"matur")]

    maturite = models.CharField(
        max_length=5,
        choices=maturite_secenek,
        default=matur,
    )

    zaman = models.DateTimeField(auto_now_add=True)


class ped_mix(models.Model):
    kilo = models.FloatField(verbose_name="Kilo (kg)")

    cc_kg = "cc"
    m2 = "m2"
    total_secenek = [(cc_kg,"cc_kg"), (m2,"m2")]
    total_mayi =  models.CharField(
        max_length=2,
        choices=total_secenek,
        default=cc_kg,
    )
    total = models.IntegerField(verbose_name="Totali kaçtan")
    sodyum = models.FloatField(verbose_name="Sodyum (meq)")
    potasyum = models.FloatField(verbose_name="Potasyum (meq)")
    kalsiyum = models.FloatField(verbose_name="Calsiyum (meq)")
    glukoz = models.FloatField(verbose_name="Glukoz (gr)")

    zaman = models.DateTimeField(auto_now_add=True)