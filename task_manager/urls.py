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
from statuses.views import (
    StatusCreateView,
    StatusDeleteView,
    StatusListView,
    StatusUpdateView,
)
from tasks.views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
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

    path('statuses/', StatusListView.as_view(), name='status_list'),
    path(
        'statuses/create/',
        StatusCreateView.as_view(),
        name='status_create',
    ),
    path(
        'statuses/<int:pk>/update/',
        StatusUpdateView.as_view(),
        name='status_update',
    ),
    path(
        'statuses/<int:pk>/delete/',
        StatusDeleteView.as_view(),
        name='status_delete',
    ),

    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path(
        'tasks/<int:pk>/update/',
        TaskUpdateView.as_view(),
        name='task_update',
    ),
    path(
        'tasks/<int:pk>/delete/',
        TaskDeleteView.as_view(),
        name='task_delete',
    ),
    path(
        'tasks/<int:pk>/',
        TaskDetailView.as_view(),
        name='task_detail',
    ),
]
