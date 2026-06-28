from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, ContactMessage

def index(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone", ""),
            message=request.POST.get("message"),
        )

        messages.success(request, "Thank you! Your message has been sent.")
        return redirect("/#contact")

    featured_project = Project.objects.filter(featured=True).first()
    projects = Project.objects.all()

    return render(
        request,
        "base.html",
        {
            "featured_project": featured_project,
            "projects": projects,
        },
    )


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(
        request,
        "home/project_detail.html",
        {
            "project": project,
        },
    )