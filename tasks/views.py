from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from .filters import TaskFilter
from .forms import LabelForm
from .models import Label, Task
from .task_forms import TaskForm


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    queryset = Task.objects.order_by('-created_at')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user

        if not form.cleaned_data.get('executor'):
            form.instance.executor = self.request.user

        messages.success(self.request, 'Tarea creada con éxito')
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tarea actualizada con éxito.')
        return super().form_valid(form)


class TaskDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Tarea eliminada con éxito.')
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'
    ordering = ['-created_at']


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label_list')

    def form_valid(self, form):
        messages.success(self.request, 'Etiqueta creada con éxito')
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label_list')

    def form_valid(self, form):
        messages.success(self.request, 'Etiqueta actualizada con éxito')
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('label_list')

    def form_valid(self, form):
        label = self.object

        if label.tasks.exists():
            messages.error(
                self.request,
                'No se puede eliminar una etiqueta asociada a una tarea.',
            )
            return self.render_to_response(
                self.get_context_data(object=label)
            )

        messages.success(self.request, 'Etiqueta eliminada con éxito')
        return super().form_valid(form)

