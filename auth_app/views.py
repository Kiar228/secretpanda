from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from auth_app.forms import Secretuser_Form
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from auth_app.models import SecretUser




@login_required(login_url="/auth/login")
def questions_view(request):

    errors = []

    if request.POST:
        if len(SecretUser.objects.filter(user=request.user)) == 0:

            info = dict(request.POST)
            del info["csrfmiddlewaretoken"]

            secretuser = SecretUser.objects.create(user=request.user)

            try:
                secretuser.hobby = info["hobby"][0]
            except:
                pass
            try:
                secretuser.fav_food = info["fav_food"][0]
            except:
                pass
            try:
                secretuser.hap_moment = info["hap_moment"][0]
            except:
                pass
            try:
                secretuser.fun_moment = info["fun_moment"][0]
            except:
                pass
            try:
                secretuser.child_dream = info["child_dream"][0]
            except:
                pass
            try:
                secretuser.job_desc = info["job_desc"][0]
            except:
                pass
            try:
                secretuser.teen_photo = request.FILES["teen_photo"]
            except:
                pass

            secretuser.save()

            return redirect("/")
        elif len(SecretUser.objects.filter(user=request.user)) != 0:
            errors.append("You have already filled out this info")




    return render(request, "auth_app/questions.html", context={"form": Secretuser_Form, "errors": errors})

@login_required(login_url="/auth/login")
def edit_questions(request):
    if len(SecretUser.objects.filter(user=request.user)) == 0:
        redirect("/auth/ask")

    errors = []

    if request.POST:
        info = dict(request.POST)
        del info["csrfmiddlewaretoken"]

        secretuser = SecretUser.objects.get(user=request.user)

        try:
            secretuser.hobby = info["hobby"][0]
        except:
            pass
        try:
            secretuser.fav_food = info["fav_food"][0]
        except:
            pass
        try:
            secretuser.hap_moment = info["hap_moment"][0]
        except:
            pass
        try:
            secretuser.fun_moment = info["fun_moment"][0]
        except:
            pass
        try:
            secretuser.child_dream = info["child_dream"][0]
        except:
            pass
        try:
            secretuser.job_desc = info["job_desc"][0]
        except:
            pass
        try:
            secretuser.teen_photo = request.FILES["teen_photo"]
        except:
            pass

        secretuser.save()

        return redirect("/")
    return render(request, "auth_app/edit_questions.html", context={"secretuser": SecretUser.objects.get(user=request.user)})
    

def login_view(request):
    errors = []
    if request.POST:
        email = request.POST['email'].lower()
        user = User.objects.filter(username=email)
        if len(user) > 0:
            user = user[0]
            login(request, user)
            secret_user = SecretUser.objects.filter(user=user)
            return redirect("/instructions")
        elif email.endswith("pandadoc.com"):
            errors.append("Can't sign in? Get in touch with Anna Shyshko")
        else:
            errors.append("Please fill in your Pandadoc email")
    return render(request, "auth_app/login.html", context={"errors": errors})
