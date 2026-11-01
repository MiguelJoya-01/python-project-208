from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Status


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = 'Nombre'
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Estado creado con éxito')
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = 'Nombre'
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Estado actualizado con éxito')
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Estado eliminado con éxito')
        return super().form_valid(form)
