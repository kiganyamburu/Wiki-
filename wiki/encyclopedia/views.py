from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def about(request):
    return render(request, "encyclopedia/about.html")

def contact(request):
    return render(request, "encyclopedia/contact.html")
