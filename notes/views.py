from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/admin/'

    def get_queryset(self):
        # return Notes.objects.filter(owner=self.request.user)
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

    def form_valid(self, form):
        # form.instance.owner = self.request.user
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        # return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_confirm_delete.html"
