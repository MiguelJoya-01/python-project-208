from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StatusForm
from .models import Status


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Estado creado con éxito')
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Estado actualizado con éxito')
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        status = self.object

        if status.tasks.exists():
            messages.error(
                self.request,
                'No se puede eliminar el estado porque está asociado a tareas.',
            )
            return self.render_to_response(
                self.get_context_data(object=status)
            )

        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                'No se puede eliminar el estado porque está asociado a tareas.',
            )
            return self.render_to_response(
                self.get_context_data(object=status)
            )

        messages.success(self.request, 'Estado eliminado con éxito')
        return response
