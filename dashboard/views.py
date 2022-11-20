from asyncio import Task
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Member
from accounts.forms import MemberChangeForm
from .models import Notification, Task


@login_required(login_url='accounts:login')
def dashboard(request):
    member = Member.objects.filter(user=request.user)[0]
    context = {
        'page':'Dashboard',
        'name':member.full_name
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='accounts:login')
def profile(request):
    member = Member.objects.filter(user = request.user)[0]
    member_info = {key:value for key, value in member.__dict__.items() if not key.startswith('__') and not callable(key)}
    form = MemberChangeForm(initial=member_info)
    if request.method == 'POST':
        form = MemberChangeForm(request.POST, instance=member)
        if form.is_valid():
            form.save()

    context = {
        'page':'Profile',
        'form':form
        }
    return render(request, 'dashboard/profile.html', context)

@login_required(login_url='accounts:login')
def tasks(request):
    curr_member = Member.objects.filter(user = request.user)[0]
    _tasks = Task.objects.filter(members = curr_member)
    context = {
        'page':'Tasks',
        'tasks': _tasks
        }
    return render(request, 'dashboard/tasks.html', context)

@login_required(login_url='accounts:login')
def notifications(request):
    curr_member = Member.objects.filter(user = request.user)[0]
    _notifications = Notification.objects.filter(target = curr_member)
    context = {
        'page':'Notifications',
        'notifications':_notifications
        }
    return render(request, 'dashboard/notifications.html', context)