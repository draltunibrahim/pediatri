from django import forms
from .models import Article, newborn_tpn, ped_mix

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]
    
class newborn_tpnForm(forms.ModelForm):
    class Meta:
        model = newborn_tpn
        fields = ["kilo","hafta",  "total", "aminoasit", "sodyum", "potasyum", "kalsiyum","glukoz", "lipit" ,"maturite"]

class ped_mixForm(forms.ModelForm):
    class Meta:
        model = ped_mix
        fields = ["kilo",  "total_mayi", "total", "sodyum", "potasyum", "kalsiyum","glukoz"]