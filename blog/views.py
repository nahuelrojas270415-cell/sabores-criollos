from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Receta
from .forms import RecetaForm

class RecetaListView(ListView):
    model = Receta
    template_name = 'blog/receta_list.html'
    context_object_name = 'recetas'
    ordering = ['-fecha']

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'blog/receta_detail.html'

class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'blog/receta_form.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class RecetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'blog/receta_form.html'
    success_url = '/'
    def test_func(self):
        return self.request.user == self.get_object().autor

class RecetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    template_name = 'blog/receta_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        return self.request.user == self.get_object().autor

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_recetas')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})