# -*- coding:utf-8 -*-

from django.views.generic.base import TemplateView
from .models import Contact, Notice


class IndexView(TemplateView):
    template_name = 'index-extreme.html'

class ProductMain(TemplateView):
    template_name = 'product.html'

class ProductDufflebag(TemplateView):
    template_name = 'product/dufflebag.html'

class ProductRaincover(TemplateView):
    template_name = 'product/raincover.html'

class ProductTawoobagpack(TemplateView):
    template_name = 'product/tawoobagpack.html'

class ProductWaistbag(TemplateView):
    template_name = 'product/waistbag.html'

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

class NoticeView(TemplateView):
    template_name = 'notice.html'

    def get_context_data(self, **kwargs):
        context = super(NoticeView, self).get_context_data(**kwargs)
        context['notices'] = Notice.objects.all().order_by('-id')
        return context

class NoticeDetail(TemplateView):
    template_name = 'notice_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NoticeDetail, self).get_context_data(**kwargs)
        context['notice'] = Notice.objects.get(id=kwargs['pk'])
        return context