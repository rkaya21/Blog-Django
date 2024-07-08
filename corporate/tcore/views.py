from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.http import HttpResponseRedirect

from tcore.models import Blog, Slider, About, Service, Category


def set_language(request, language):
    try:
        referer_path = urlparse(request.META.get("HTTP_REFERER")).path
        view = resolve(referer_path)
    except Resolver404:
        return HttpResponseRedirect("/")

    translation.activate(language)

    next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)

    return HttpResponseRedirect(next_url)


class BaseView(object):
    """
      View'ler için ortak context sınıfı
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()  # Tüm kategorileri context'e Ekle
        return context


class IndexView(ListView):
    """
    Ana Sayfam için oluşturduğum View
    """
    template_name = 'index.html'
    model = Slider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all()  # Tüm Slider verilerini Ekle
        context['Abouts'] = About.objects.first()  # İlk hakkımdamı Ekle
        context['Services'] = Service.objects.all()  # Tüm servis verilerini Ekle
        context['Blogs'] = Blog.objects.all()  # Tüm Blog verilerini Ekle
        return context


class AboutView(ListView):
    """
    Hakkımda Sayfam için oluşturduğum View
    """
    template_name = 'about.html'
    context_object_name = "Abouts"
    queryset = About.objects.first()


class ServiceView(ListView):
    """
    Hizmetler kısmı için oluşturduğum View.
    """
    template_name = 'services.html'
    context_object_name = "Services"
    queryset = Service.objects.all()


class BlogView(BaseView, ListView):  # error: BaseView önde olmalı.
    """
    Blog listeleri sayfası için oluşturduğum View
    """
    template_name = 'blog.html'
    context_object_name = "Blogs"
    queryset = Blog.objects.all()


class BlogDetailView(BaseView, DetailView):  # error: BaseView önde olmalı.
    """
    Blog listesi sayfasında Detaylar butonuna bastığında açılan detaylar sayfası için View
    """
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = "blog"
    slug_url_kwarg = "slug"


class CategoryDetailView(BaseView, ListView):  # error: BaseView önde olmalı.
    """
    Blog listelerini Dashboard'dan belirli kategoriye göre ekliyorum.Örneğin,
    Felsefe kategorisine bastığınızda Felsefe ile ilgili blogları sorgular.
    """
    model = Blog
    template_name = 'category-details.html'
    context_object_name = "Blogs"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=slug)
        return Blog.objects.filter(category=category)


class ContactView(TemplateView):
    """
    İletişime geçilmesi için oluşturduğum View.
    """
    template_name = 'contact.html'
