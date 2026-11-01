import django_filters

from .models import Label, Task
from statuses.models import Status
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
    )

    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
    )

    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        label='Solo mis tareas',
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'self_tasks']
