# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
def index(request):
    if "words" not in request.session:
        request.session["words"]=[]
    return render(request, "session_words/index.html")
def add_word(request):
    if len(request.POST["word"])<1:
        return redirect("/")
    if "font" in request.POST:
        font="2em"
    else:
        font="1em"
    allwords = request.session["words"]
    allwords.append({
        "word":request.POST["word"],
        "color":request.POST["color"],
        "font":font,
        "time":strftime("%I:%M:%S%p, %B %d, %Y", localtime())
    })
    request.session["words"] = allwords
    return redirect("/session_words")
def clear(request):
    request.session.clear()
    return redirect("/session_words")