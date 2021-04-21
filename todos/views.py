from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserUpdateForm, ProfileUpdateForm, TodoUpdateForm, NotesUpdateForm
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView
from .models import Todo, Notes


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('todos-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        todos = Todo.objects.filter(user=request.user)
        notes = Notes.objects.filter(user=request.user)
        context = {
            'u_form': user_form,
            'p_form': profile_form,
            'todos': todos,
            'notes': notes,
        }
    return render(request, 'todos/profile.html', context)


# TODOS
class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'important', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['title', 'important', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo

    success_url = '/profile'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False


# NOTES
class NotesDetailView(DetailView):
    model = Notes


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True
        return False


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes

    success_url = '/profile'

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True
        return False
