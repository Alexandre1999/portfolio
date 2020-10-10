import os

from django.contrib.auth import logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ProjectForm, BioForm

from .models import Project, Bio


def home_view(request):
    projects = Project.objects.filter(active=True, featured=True).order_by('-date')[0:3]
    bio = get_object_or_404(Bio, id=1)
    context = {
        'projects': projects,
        'bio': bio
    }
    return render(request, 'home.html', context)


def projects_view(request):
    projects = Project.objects.filter(active=True).order_by('-date')

    page = request.GET.get('page')
    paginator = Paginator(projects, 6)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        'projects': projects
    }

    return render(request, 'projects.html', context)


def project_detail_view(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project': project
    }

    return render(request, 'detail_project.html', context)


@login_required(login_url="base:home")
def create_project_view(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('base:projects')

    context = {
        'form': form,
        'context': "Project"
    }
    return render(request, 'form.html', context)


@login_required(login_url="base:home")
def update_project_view(request, slug):
    project = Project.objects.get(slug=slug)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
        return redirect('base:projects')

    context = {
        'form': form,
        'context': "Project"

    }
    return render(request, 'form.html', context)


@login_required(login_url="base:home")
def delete_project_view(request, slug):
    project = Project.objects.get(slug=slug)

    if request.method == 'POST':
        project.delete()
        return redirect('base:projects')
    context = {'item': project}
    return render(request, 'delete.html', context)


@login_required(login_url="base:home")
def update_bio_view(request):
    bio = get_object_or_404(Bio, id=1)
    form = BioForm(instance=bio)

    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            form.save()
        return redirect('base:home')

    context = {
        'form': form,
        'context': "Bio"
    }
    return render(request, 'form.html', context)


def send_email_view(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['ivanraymond99@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'email_sent.html')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/base")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


def logout_view(request):
    logout(request)
    return redirect("base:home")
