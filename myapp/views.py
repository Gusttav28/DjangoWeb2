from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import project, Task
from .forms import create_new_task, create_new_project


def index(request):
    title = "Gustavo's projects" 
    return render(request, "index.html", {
        'title':title
    })

def user_hello(request, username):
    return HttpResponse(f"<h1> This is the index and, <h2> Hi! {username}<h2> <h1>", request, 'index.html')

def resume(request):
    user_resume = "Gustavo Resume"
    return render(request, "resume.html", {
        'user_resume':user_resume
    })

def projects(request):
    # projects = list(project.objects.values())
    projects = project.objects.all()
    return render(request, "projects/projects.html", {
        'projects':projects
        })

def task(request):
    # task = Task.objects.get(id = id)
    # task = get_object_or_404(Task, id = id)
    tasks = Task.objects.all()
    return render(request, "tasks/task.html", {
        'tasks': tasks
    })     


def create_task(request):
    # user_title = request.POST['title']
    # print(user_title)
    # user_description = request.POST['description']
    # print(user_description)
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': create_new_task()
    })
    else:
        Task.objects.create(Title=request.POST['title'], Description=request.POST['description'], Project_id=2)
        return redirect('task')
    

def create_project(request):
    if request.method == 'GET':
        return render(request, "projects/create_project.html", {
        'form': create_new_project()
    })
    else:
        projectt = project.objects.create(name=request.POST['name'])
        print(projectt)
        return redirect('projects')
        # return render(request, "projects/create_project.html", {
        # 'form': create_new_project()})
        # # return redirect('/projects/')

def project_details(request, id):
    # projects_id = project.objects.get(id=id)

    projects_id = get_object_or_404(project, id = id)
    print(projects_id)
    tasks = Task.objects.filter(Project_id=id)
    return render(request, 'projects/detail.html', {
        'projects_id': projects_id,
        'tasks':tasks
    })
    

    
    

    

# Create your views here.
            