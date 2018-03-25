# -*- coding:utf-8 -*-

from django.views.generic.base import TemplateView
from .models import Contact


class IndexView(TemplateView):
    template_name = 'index-extreme.html'

class ProductMain(TemplateView):
    template_name = 'product.html'


class ProductOne(TemplateView):
    template_name = 'product1.html'

class ProductTwo(TemplateView):
    template_name = 'product2.html'

class AboutView(TemplateView):
    template_name = 'who-we-are.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('txtname', 'Unknown')
        email = request.POST.get('txtemail', 'Unknown')
        content = request.POST.get('txtmessage', None)
        result = Contact(
            name=name,
            email=email,
            content=content
        )
        result.save()
        return super(ContactView, self).get(request, *args, **kwargs)