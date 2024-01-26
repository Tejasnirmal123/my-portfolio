from django.shortcuts import render, redirect
from .models import Project, Skill, User
from .forms import ProjectForm, QuestionForm, SkillForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects':projects, 'skills':skills,'detailedSkills':detailedSkills}
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
   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        new_user = User(name=name, email=email, phone=phone, message=message)
        new_user.save()

        send_mail(
            'Message From'+ name,
            email,
            message,
            ['tejasnirmal11@gmail.com'],
        )
        return HttpResponse("FORM SUBMISSION IS SUCCESSFUL and YOUR MAIL IS RECEIVED")



    return render(request,'base/contact.html')

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

