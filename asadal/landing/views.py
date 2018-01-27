# -*- coding:utf-8 -*-

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductOne(TemplateView):
    template_name = 'product1.html'

class ProductTwo(TemplateView):
    template_name = 'product2.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactUsView(TemplateView):
    template_name = 'contactus.html'