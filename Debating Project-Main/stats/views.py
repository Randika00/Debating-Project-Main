from sqlite3 import Timestamp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from .models import Tournament, Debater, Institution, User, Motion, Round, Score


def index(request):
    return render(request, "stats/index.html")
    # return HttpResponse("Index")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "stats/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "stats/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "stats/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "stats/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "stats/register.html")


# class ListingForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(
#         attrs={'autofocus': True, 'class': 'formtitle'}))
#     category = forms.CharField(label='Category', max_length=100, widget=forms.TextInput(
#         attrs={'class': 'formcategory'}))
#     description = forms.CharField(label='Description', max_length='150', widget=forms.Textarea(
#         attrs={'rows': 3, 'class': 'formdescription'}))
#     stbid = forms.IntegerField(
#         label='Starting Bid', widget=forms.NumberInput(attrs={'class': 'formbid'}))
#     picture = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={'class': 'formpic'}))
# class CommentForm(forms.Form):
#     comment = forms.CharField(label="Comment", max_length=300, widget=forms.TextInput(
#         attrs={'class': 'formcomment'}))

def getspeaks(request):
    if request.method == 'POST':
        n = int(request.POST["rounds"])
        raw = (request.POST["scores"]).strip()
        url = request.POST.get('url')
        slug = request.POST.get('slug')
        org = request.POST["org"]
        
        rows = [line.strip() for line in raw.split('\n')]
        rows.pop(0)
        data = {}
        for r in rows:
            r = r.split('\t')
            data[r[1]] = []
            for i in range(n):
                score = r[i+3]
                if score != '—':
                    score = float(score)
                data[r[1]].append(score)
        print(f"data: {data}")
        return HttpResponse("Success")
    
    elif request.method == 'GET':
        ins = Institution.objects.all()
        return render(request, "stats/formpage.html",{"ins":ins})


def showdebaters(request):
    deb = Debater.objects.all()
    return render(request, "stats/alldebaters.html", {"debaters": deb})


def showtourneys(request):
    tourneys = Tournament.objects.all()
    return render(request, "stats/tournaments.html", {"tournaments": tourneys})


def show_ins(request):
    ins = Institution.objects.filter(active=True)
    return render(request, "stats/institutions.html", {"institutions": ins})
