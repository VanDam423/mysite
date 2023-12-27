from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post_list/', views.post_list, name='post_list'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='register'),
    path('economic_news/', views.economic_news, name='economic_news'),
    path('politic_news/', views.politic_news, name='politic_news'),
    path('interesting_news/', views.interesting_news, name='interesting_news'),
    path('main_news/', views.main_news, name='main_news'),
    path('culture_news/', views.culture_news, name='culture_news'),
]