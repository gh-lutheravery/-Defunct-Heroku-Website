from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    AnnouncementDetailView,
                    AnnouncementCreateView,
                    AnnouncementUpdateView,
                    AnnouncementDeleteView,
                    SearchView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='antiquity-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='antiquity-about'),
    path('search_results/', SearchView.as_view(), name='antiquity-search'),
    path('ann/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='ann-delete'),
    path('ann/<int:pk>/', AnnouncementDetailView.as_view(), name='ann-detail'),
    path('ann/new/', AnnouncementCreateView.as_view(), name='ann-create'),
    path('ann/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='ann-update'),
]

# <app>/<model>_<viewtype>.html
