from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from .models import Type

# Create your views here.


def index(request):
    query_result = Type.get_all_types_raw()
    template = loader.get_template("hardware/index.html")
    context = {
        "query_result": query_result,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(template.render(context,request))
    # return HttpResponse("Hello user. you're at the hardware request index page. These are the options:")
