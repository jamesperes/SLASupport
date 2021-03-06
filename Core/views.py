from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Chamado, Area, Problema, Categoria_Problema
from .forms import ChamadoCreateForm, ChamadoDetailForm, ChamadoUpdateForm



class ChamadoListView(LoginRequiredMixin, ListView):

    model = Chamado
    context_object_name = 'chamado'
    paginate_by = 15
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'



class ChamadoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Chamado
    form_class = ChamadoCreateForm
    success_url = reverse_lazy('home')
    success_message = "Ocorrência aberta com Sucesso no Sistema."
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'

    def get_initial(self):

        user = self.request.user
        initial = {'criador': user}
        return initial


class ChamadoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Chamado
    form_class = ChamadoUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
    success_message = "Ocorrência Alterada com Sucesso!"
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'


class ChamadoDetailView(DetailView):
    model = Chamado
    template_name_suffix = '_detail_form'
    form_class = ChamadoDetailForm


@login_required
def content_details(request):

    if request.method == 'GET' and 'problema' in request.GET:
        area_id = request.GET.get('problema')
        problemas = Problema.objects.filter(area_id=area_id).order_by('desc_problema')

        return render (request, 'misc/problemas_dropdown_list.html', {'problemas' : problemas})

    elif request.method == 'GET' and 'cat_problema' in request.GET:
        problema_id = request.GET.get('cat_problema')
        cat_problemas = Categoria_Problema.objects.filter(
                problema_id=problema_id).values(
                    'id',
                    'problema__desc_problema',
                    'desc_categoria_problema',
                    'sla',
                    'tipo_manutencao',
                    'origem'
                )
        return render (request, 'misc/cat_problemas_options_list.html', {'cat_problemas' : cat_problemas} )