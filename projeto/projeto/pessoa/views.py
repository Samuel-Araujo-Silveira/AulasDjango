from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pessoa, PessoaJuridica

def add(request):
    return HttpResponse("<h1> OI! AQUI VAI ADD' </h1>")

def list(request):

    if request.GET:
        
        dic = {}
        
        for key, val in request.GET.lists():
            dic.update({key + "__contains": val[0]})

        pessoas = Pessoa.objects.all().filter(**dic)
    else:
        pessoas = Pessoa.objects.all()

    template = loader.get_template("pessoa/index.html")
    context = { 'pessoas': pessoas}
    return HttpResponse(template.render(context,request))
    ## return render(request, 'pessoa/index.html', {'pessoas': pessoas})

def refresh(request):
    return HttpResponse("<h1> OI! AQUI VAI atualizar' </h1>")

def remove(request):
    return HttpResponse("<h1> OI! AQUI VAI remover' </h1>")

def detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    template = loader.get_template("pessoa/detail.html")
    context = {'pessoa':pessoa}
    return HttpResponse(template.render(context,request))


def filterCpf(request, query):
    pessoas = Pessoa.objects.all().filter(cpf__contains=query)

    template = loader.get_template("pessoa/filter.html")
    context = {'pessoas':pessoas}

    return HttpResponse(template.render(context,request))