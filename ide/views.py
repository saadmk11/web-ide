from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class WebIDEView(LoginRequiredMixin, TemplateView):
    template_name = 'ide/terminal.html'
    login_url = '/admin/login/'
