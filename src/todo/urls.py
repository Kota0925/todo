from django.urls import path
from .views import todoListView, todoDetailView, todoCreateView, todoUpdateView, todoDeleteView

urlpatterns = [
    path("list/", todoListView, name="todo-list"),
    path("detail/<int:number>/", todoDetailView, name="todo-detail"),
    path("create/", todoCreateView, name="todo-create"),
    path("update/<int:number>/", todoUpdateView, name="todo-update"),
    path("delete/<int:number>/", todoDeleteView, name="todo-delete"),
]
