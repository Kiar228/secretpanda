from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from auth_app.models import SecretUser
from django.contrib.auth.models import User
from django.db.models import Q
import random
from django.http.response import HttpResponse

# Create your views here.
@login_required(login_url="/auth/login", redirect_field_name=None)
def homepage(request):
    if len(SecretUser.objects.filter(user=request.user)) == 0:
        return redirect("/auth/ask")

    all_users = User.objects.all()
    all_users = filter(lambda x: x.username != "admin", all_users)

    user_picked = SecretUser.objects.get(user=request.user).picked_user
    widthlist = [2,3,5,7,9]
    return render(request, "santa_app/homepage.html", context={"all_users": list(all_users), "user_picked": user_picked, "range1": widthlist, "range2": widthlist[::-1]})


@login_required(login_url="/auth/login", redirect_field_name=None)
def instruction_view(request):
    if len(SecretUser.objects.filter(user=request.user)) == 0:
        ask = True
    else:
        ask = False
    return render(request, "santa_app/instructions.html", context={"ask": ask})


@login_required(login_url="/auth/login", redirect_field_name=None)
def get_giftee(request):

    santa_user = SecretUser.objects.get(user=request.user)

    if santa_user.picked_user:
        return HttpResponse(santa_user.picked_user.first_name + " " + santa_user.picked_user.last_name)
    else:
        
        picked_users = []
        for u in SecretUser.objects.filter(~Q(picked_user=None)):
            picked_users.append(u.picked_user)


        possible_to_pick = []
        for u in User.objects.all():
            if (u not in picked_users) and (u != request.user):
                possible_to_pick.append(u)

        random_id = round(random.random() * (len(possible_to_pick) - 1))
        santa_user.picked_user = possible_to_pick[random_id]
        santa_user.save()

        return HttpResponse(santa_user.picked_user.first_name + " " + santa_user.picked_user.last_name)
        
