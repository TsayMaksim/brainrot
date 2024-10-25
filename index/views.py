from django.shortcuts import render, redirect
from .models import Category, VideoModel, User, Comments
from django.views import View
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
def home_page(request):
    video = VideoModel.objects.all()
    categories = Category.objects.all()
    context = {'video': video , 'categories': categories}
    return render(request, 'home.html', context)


def video_page(request, pk):
    video = VideoModel.objects.all()
    context = {'video': video}
    return render(request, 'video.html', context)


def category_page(request, pk):
    category = Category.objects.get(id=pk)
    exact_video = VideoModel.objects.filter(video_category=category)
    context = {'category': category, 'video': exact_video}
    return render(request, 'category.html', context)


def user_page(request):
    return render(request, 'user.html')


def comments_page(request):
    return render(request, 'comments.html')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password2)
            user.save()
            login(request, user)
            return redirect('/')
        context = {'form': RegForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')
