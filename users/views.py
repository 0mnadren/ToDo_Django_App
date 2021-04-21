from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm
from .models import Video
from django.views.decorators.csrf import csrf_exempt


def home(request):
    videos = Video.objects.all()
    return render(request, 'users/home.html', {'videos': videos})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! '
                                      f'You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

