from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from car.models import Category, Comment
from home.models import UserProfile
from reservation.models import Reserve
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user  # access user session informations
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {

        'category': category,
        'profile': profile,

    }
    return render(request, 'profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,instance= request.user.userprofile )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account has been updated!')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance= request.user.userprofile)
        context = {

            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,

        }
        return render(request,'user_update.html', context);

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password changed!!')
            return redirect('changepassword')
        else:
            messages.error(request,'Please be sure that inputs are same or old password is true!! <br>' + str(form.errors))
            return  HttpResponseRedirect('changepassword')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'change_password.html', {
            'form' : form, 'category': category
        })

@login_required(login_url = '/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id = current_user.id)
    context = {
        'category': category,
        'comments': comments,
    }
    return  render(request, 'user_comments.html', context)


@login_required(login_url = '/login')
def deletecomment(request , id):
    current_user = request.user
    comments = Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted!')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url = '/login')
def reservations(request):
    category = Category.objects.all()
    current_user = request.user
    reservations = Reserve.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'reservations': reservations,
    }
    return render(request, 'user_reservations.html', context)

@login_required(login_url = '/login')
def reservationdetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    reservation = Reserve.objects.filter(user_id=current_user.id, id=id)
    reservationitem = Reserve.objects.filter(id=id)
    context = {
        'category': category,
        'reservation': reservation,
        'reservationitem': reservationitem,
    }
    return render(request, 'user_reservation_detail.html', context)