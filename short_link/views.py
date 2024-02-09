from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from .models import Links
from django.views.generic import ListView, DeleteView
from .forms import LinkForm
import re
from django.contrib import messages


class LinksView(ListView):
    model = Links
    template_name = 'short_link/short_link.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LinksView, self).get_context_data(**kwargs)
        link = Links.objects.filter(user=self.request.user.id).all().order_by('-id')
        form = LinkForm()
        ctx['title'] = 'Сокращение ссылок'
        ctx['links'] = link
        ctx['form'] = form
        return ctx

    @staticmethod
    def post(request, *args, **kwargs):
        post = request.POST.copy()
        post['user'] = request.user
        post['slug'] = str(request.user.id) + '-' + str(request.POST['slug'])

        request.POST = post
        form = LinkForm(request.POST)

        link_new = request.POST['slug']
        short = Links.objects.filter(slug=link_new).all()

        if not short:
            if re.match(r'^[A-Za-z0-9_-]+$', link_new):
                if form.is_valid():
                    link = form.save(commit=False)
                    link.save()
                    form = LinkForm()
                    messages.success(request, 'Ссылка добавлена')

        link = Links.objects.filter(user=request.user.id).all().order_by('-id')

        data = {
            'title': 'Сокращение ссылок',
            'form': form,
            'links': link,
        }

        return render(request, 'short_link/short_link.html', data)


class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Links
    success_url = '/short'

    def test_func(self):
        links = self.get_object()
        if self.request.user == links.user:
            return True
        return False
