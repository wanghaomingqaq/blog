from django.shortcuts import render
from blog01 import models
from markdown import markdown

# Create your views here.
def index(request):
    note = models.Article.objects.all()
    return render(request,'index.html',locals())

def article(request,article_id):
    note = models.Article.objects.get(id=int(article_id))
    note.content = markdown(note.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return render(request,'blog-single.html',locals())