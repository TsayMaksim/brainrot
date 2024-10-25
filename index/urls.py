from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page, name='home'),
    path('video/<int:pk>', views.video_page),
    path('category/<int:pk>', views.category_page),
    path('user_page/<int:pk>', views.user_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view)
]
