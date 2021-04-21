from django.urls import path
from . import views as todos_views
from .views import (
    TodoUpdateView,
    TodoDetailView,
    TodoCreateView,
    TodoDeleteView,
    NotesDetailView,
    NotesCreateView,
    NotesUpdateView,
    NotesDeleteView,
)


urlpatterns = [
    path('', todos_views.profile, name='todos-profile'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todo/new/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),

    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('notes/new/', NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(), name='notes-delete'),
]
