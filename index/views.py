from django.shortcuts import render
from .models import Category, VideoModel, User, Comments


# Create your views here.
def home_page(request):
    video = VideoModel.objects.all()
    categories = Category.objects.all()
    context = {'video': video , 'categories': categories}
    return render(request, 'home.html', context)


def video_page(request, pk):
    video = VideoModel.objects.get(id=pk)
    context = {'video': video}
    return render(request, 'video.html', context)


def category_page(request, pk):
    category = Category.objects.get(id=pk)
    exact_video = VideoModel.object.filter(video_category=category)
    context = {'category': category, 'video': exact_video}
    return render(request, 'category.html', context)


def user_page(request):
    return render(request, 'user.html')


def comments_page(request):
    return render(request, 'comments.html')