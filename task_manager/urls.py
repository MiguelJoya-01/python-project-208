
from django.contrib import admin
from django.urls import path

from task_manager.views import index
from users.views import (
    CustomLoginView,
    CustomLogoutView,
    UserCreateView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    path('users/', UserListView.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path(
        'users/<int:pk>/update/',
        UserUpdateView.as_view(),
        name='user_update',
    ),
    path(
        'users/<int:pk>/delete/',
        UserDeleteView.as_view(),
        name='user_delete',
    ),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

