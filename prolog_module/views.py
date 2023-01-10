from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .CreateKBForm import CreateKBForm
from .Genealogical_Tree import Genealogical_Tree


# Create your views here.
def prolog_main(request):
    if request.method == 'POST':
        form = CreateKBForm(request.POST)
        if form.is_valid():
            pass
        #return HttpResponseRedirect('/created_knowledge_base')
    else:
        form = CreateKBForm()
    template = "prolog_module/prolog_module.html"

    context = {
        'form': form,
    }
    return render(request=request, template_name=template, context=context)
