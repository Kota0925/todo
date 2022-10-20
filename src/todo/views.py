from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoModel
from .forms import TodoFormClass

# 日報一覧画面
def todoListView(request):
    objectList = TodoModel.objects.all()
    ctx = {"objectList": objectList}
    template_name = "todo-list.html"
    return render(request, template_name, ctx)

# 日報詳細画面
def todoDetailView(request, number):
    object = get_object_or_404(TodoModel, pk=number)
    ctx = {"object": object}
    template_name = "todo-detail.html"
    return render(request, template_name, ctx)

# 日報作成画面
def todoCreateView(request):
    form = TodoFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = request.POST["title"]
        content = request.POST["content"]
        object = TodoModel(title=title, content=content)
        object.save()
        return redirect("todo-list")
    template_name = "todo-create.html"
    return render(request, template_name, ctx)

# 日報更新画面
def todoUpdateView(request, number):
    object = get_object_or_404(TodoModel, pk=number)
    initialValues = {"title": object.title, "content": object.content}
    form = TodoFormClass(request.POST or initialValues)
    ctx = {"form": form, "object": object}
    if request.POST:
        if form.is_valid():
            object.title = form.cleaned_data["title"]
            object.content = form.cleaned_data["content"]
            object.save()
            return redirect("todo-detail", object.pk)
    template_name = "todo-update.html"
    return render(request, template_name, ctx)

# 日報削除画面
def todoDeleteView(request, number):
    object = get_object_or_404(TodoModel, pk=number)
    ctx = {"object": object}
    if "done" in request.POST:
        object.delete()
        return redirect("todo-list")
    elif "cancel" in request.POST:
        return redirect("todo-detail", object.pk)
    template_name = "todo-delete.html"
    return render(request, template_name, ctx)
