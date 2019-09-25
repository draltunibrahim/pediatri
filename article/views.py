from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm, newborn_tpnForm, ped_mixForm
from django.contrib import messages
from .models import Article, Comment, newborn_tpn
from django.contrib.auth.decorators import login_required
# Create your views here.
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles" : articles})

    articles = Article.objects.all()

    return render(request, "articles.html", {"articles" : articles})


def index(request):
    context = {
        "numbers" : [1,2,3,4,5],
        "number1" : 30,
        "number2" : 200
    }
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)
@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():

        article =  form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("article:dashboard")

    return render(request, "addarticle.html",{"form" : form})

def detail(request, id):
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()


    return render(request , "detail.html", {"article" : article, "comments" : comments})

    


@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article =  form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("article:dashboard")

    return render(request, "update.html",{"form" : form})
@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, "Makale başarı ile silindi")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article, id = id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()

        messages.success(request, "Yorum başarıyla eklendi")

    return redirect(reverse("article:detail", kwargs={"id" : id}))      

def newborn_tpn(request):
    form = newborn_tpnForm(request.POST or None)
    
    context = {
        "form" : form
    }

    if form.is_valid():
        
        kilo = form.cleaned_data.get("kilo")
        hafta = form.cleaned_data.get("hafta")
        total = form.cleaned_data.get("total")
        aminoasit = form.cleaned_data.get("aminoasit")
        sodyum = form.cleaned_data.get("sodyum")
        potasyum = form.cleaned_data.get("potasyum")
        kalsiyum = form.cleaned_data.get("kalsiyum")
        glukoz = form.cleaned_data.get("glukoz")
        lipit = form.cleaned_data.get("lipit")
        maturite = form.cleaned_data.get("maturite")
        
        total_mayi = total * kilo
        aminoasit_cc = 10*aminoasit*kilo
        sodyum_cc = 2*sodyum*kilo
        potasyum_cc = (potasyum*kilo)/3
        potasyum_cc = round(potasyum_cc,1)
        kalsiyum_cc = (kalsiyum*kilo)/100
            #if hafta < 38: 
             #   cernevit = kilo*1
               # magnesyum = kilo/10
            
        cernevit = kilo*2
        magnesyum = (kilo*2)/10
        trakutil = (kilo*2)/10
        lipit_cc = lipit*kilo*5
        
        if maturite == "pm":
            cernevit = kilo*1
            magnesyum = (kilo*1)/10
        
        


        
        total_mayi_haric = float(aminoasit_cc) + float(sodyum_cc) + kalsiyum_cc + potasyum_cc + cernevit + magnesyum + trakutil + lipit_cc
        total_mayi_haric = round(total_mayi_haric,1)
        glikoz_mayi = total_mayi - total_mayi_haric
        glikoz_mayi = round(glikoz_mayi,1)
        

        glikoz_gr = (glukoz * kilo * 1.44)
        glikoz_gr = round(glikoz_gr,1)
        #glikoz_mayi_10 = (glikoz_mayi*5)/100
        #dex_10 = glikoz_gr - glikoz_mayi_10
        #dex_10 = dex_10*20
        #dex_10 = round(dex_10,1)
        #dex_5 = glikoz_mayi - dex_10
        #dex_5 = round(dex_5,1)

        a = glikoz_gr
        b_5 = (glikoz_mayi*5)/100
        b_10 = (glikoz_mayi*10)/100
        b_30 = (glikoz_mayi*30)/100

        if a<b_30 and a>b_10:
            x = (glikoz_mayi*10)/100
            dex_30 = (glikoz_gr - x)*5
            dex_30 = round(dex_30,0)
            dex_10 = glikoz_mayi - dex_30
            dex_10 = round(dex_10,0)
            dex_5 = 0
        if a<b_10 and a>b_5:
            x = (glikoz_mayi*5)/100
            dex_10 = (glikoz_gr -x)*20
            dex_10 = round(dex_10,0)
            dex_5 = glikoz_mayi-dex_10
            dex_5 = round(dex_5,0)
            dex_30 = 0
        if a>b_30:
            dex_30 = glikoz_mayi
            dex_10 = 0
            dex_5 = 0


        cc_st = total_mayi/24
        cc_st = round(cc_st,1)

        
            
        


        context2 = {
            "kilo" : kilo,
            "total_mayi" : total_mayi,
            "aminoasit_cc" : aminoasit_cc,
            "sodyum_cc" : sodyum_cc,
            "potasyum_cc" : potasyum_cc,
            "kalsiyum_cc" : kalsiyum_cc,
            "total_mayi_haric" : total_mayi_haric,
            "glikoz_mayi" : glikoz_mayi,
            "glikoz_gr" : glikoz_gr,
            "dex_30" : dex_30,
            "dex_10" : dex_10,
            "dex_5" : dex_5,
            "cc_st" : cc_st,
            "post2" : "post2",
            "cernevit" : cernevit,
            "magnesyum" : magnesyum,
            "trakutil" : trakutil,
            "lipit_cc" : lipit_cc,
            "maturite" : maturite,
 
            }
        
        newborn_tpn =  form.save(commit = False)
        newborn_tpn.save()
        return render(request,"newborn_tpn.html", context2)

    return render(request,"newborn_tpn.html", context)


def ped_mix(request):
    form = ped_mixForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        kilo = form.cleaned_data.get("kilo")
        total_mayi = form.cleaned_data.get("total_mayi")
        total = form.cleaned_data.get("total")
        sodyum = form.cleaned_data.get("sodyum")
        potasyum = form.cleaned_data.get("potasyum")
        kalsiyum = form.cleaned_data.get("kalsiyum")
        glukoz = form.cleaned_data.get("glukoz")


        m2 = (4*kilo)+7
        m2 = m2/(90+kilo)
        m2 = round(m2,1)
        total_mayi_cc = m2*total
        total_mayi_cc = round(total_mayi_cc,0)
        if total_mayi == "cc":
            total_mayi_cc = kilo*total
            total_mayi_cc = round(total_mayi_cc,0)
        
        sodyum_cc = 2*sodyum*kilo
        potasyum_cc = (potasyum*kilo)/3
        potasyum_cc = round(potasyum_cc,1)
        kalsiyum_cc = (kalsiyum*kilo)/100

        total_mayi_haric = sodyum_cc + potasyum_cc + kalsiyum_cc
        total_mayi_haric = round(total_mayi_haric,1)
        glikoz_mayi = total_mayi_cc - total_mayi_haric
        glikoz_mayi = round(glikoz_mayi,1)

        glikoz_gr = (glukoz * kilo * 1.44)
        glikoz_gr = round(glikoz_gr,1)
        
        a = glikoz_gr
        b_5 = (glikoz_mayi*5)/100
        b_10 = (glikoz_mayi*10)/100
        b_30 = (glikoz_mayi*30)/100

        if a<b_30 and a>b_10:
            x = (glikoz_mayi*10)/100
            dex_30 = (glikoz_gr - x)*5
            dex_30 = round(dex_30,0)
            dex_10 = glikoz_mayi - dex_30
            dex_10 = round(dex_10,0)
            dex_5 = 0
        if a<b_10 and a>b_5:
            x = (glikoz_mayi*5)/100
            dex_10 = (glikoz_gr -x)*20
            dex_10 = round(dex_10,0)
            dex_5 = glikoz_mayi-dex_10
            dex_5 = round(dex_5,0)
            dex_30 = 0
        if a>b_30:
            dex_30 = glikoz_mayi
            dex_10 = 0
            dex_5 = 0



        cc_st = total_mayi_cc/24
        cc_st = round(cc_st,1)

        


        context2 = {
            "kilo" : kilo,
            "post2" : "post2",
            "total_mayi_cc" : total_mayi_cc,
            "m2" : m2,
            "sodyum_cc" : sodyum_cc,
            "potasyum_cc" : potasyum_cc,
            "kalsiyum_cc" : kalsiyum_cc,
            "total_mayi_haric" : total_mayi_haric,
            "dex_30" : dex_30,
            "dex_10" : dex_10,
            "dex_5" : dex_5,
            "cc_st" : cc_st,
            "glikoz_gr" : glikoz_gr,
            "glikoz_mayi" : glikoz_mayi,
        }  
        



        ped_mix =  form.save(commit = False)
        ped_mix.save()
        return render(request,"ped_mix.html", context2)

    return render(request,"ped_mix.html", context)
