from django.shortcuts import render, redirect
from .models import Project, Skill, User, Message
from .forms import ProjectForm, QuestionForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent Successfully. ')
            return redirect('/')



    context = {'projects':projects, 'skills':skills,
               'detailedSkills':detailedSkills, 'form':form}
    return render(request,'base/home.html', context) 


def projectPage(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request, 'base/project.html', context)

@login_required()
def addProject(request):
    form = ProjectForm

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'base/project_form.html', context)

@login_required()
def editProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'base/project_form.html', context)

def contact(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent Successfully. ')
            return redirect('contact')

    context = {'form':form}
    return render(request,'base/contact.html', context)

def chartPage(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        form.save()
        
        return redirect('chart')
    return render(request, 'base/chart.html', {'form':form})

@login_required()
def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'base/skill_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox':inbox, 'unreadCount':unreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message':message}
    return render(request, 'base/message.html', context)

