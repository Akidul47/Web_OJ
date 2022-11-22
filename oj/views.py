from multiprocessing import context
from termios import VT1
from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CompilerModelForm
from .models import CompilerModel


class IndexView(CreateView):
    template_name = "oj/index.html"
    form_class = CompilerModelForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class SubmitView(TemplateView):
    template_name = "oj/success.html"
    file_data = open(r"data.txt", "r", encoding='UTF-8')
    v1 = file_data.read()
    def get_context_data(self, **kwargs):
        context = locals()
        context['v1'] = self.v1
        return context

# class SubmitView(TemplateView):
#     template_name = "oj/success.html"
#     v = 2
#     def get(self, request, *args, **keyargs):
#         context = locals()
# django-oj-master/data.txt
#         context['v'] = self.v
#         return render(self.template_name, context)
