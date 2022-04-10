from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post, Announcement
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    posts = search(request)
    if posts:
        context['posts'] = posts

    return render(request, 'antiquity/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'antiquity/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author of article to current logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # homepage

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class SearchView(PostListView):
    template_name = 'antiquity/search_results.html'
    context_object_name = 'query_posts'

    def get_queryset(self):
        query = self.request.GET.get('search_bar')
        query_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))

        paginator = Paginator(query_posts, self.paginate_by)

        return query_posts


class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/'

    def test_func(self):
        ann = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return False


class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ann = self.get_object()
        if self.request.user == ann.author:
            return True
        else:
            return False


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'antiquity/ann_detail.html'


def about(request):
    return render(request, 'antiquity/about.html', {'title': 'About'})
