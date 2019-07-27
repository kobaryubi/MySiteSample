import json

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from MySite.settings.base import *
from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *

from .models import *
from .forms import *

class BlogsListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = "blogs_list"
    ordering = "updated_at"
    paginate_by = 5
    template_name = "blog_app/blogs_list.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_queryset(self):
        queryset = Blog.objects.all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog_app/blog_detail.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog_app/create_blog.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = reverse_lazy("blog_app:blogs_list")
