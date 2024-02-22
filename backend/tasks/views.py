from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from tasks.models import Task

# Create your views here.

require_http_methods(["GET"])


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})


@require_http_methods(["POST"])
def add_task(request):
    title = request.POST.get("title")
    due_date = request.POST.get("due_date")

    if not title or not due_date:
        messages.add_message(
            request,
            messages.ERROR,
            "All fields are required.",
        )
    else:
        Task.objects.create(title=title, due_date=due_date)

    return redirect("index")
