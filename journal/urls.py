# journal/urls.py
from django.urls import path
from .views import (
    JournalEntryListCreateView,
    JournalEntryRetrieveUpdateDestroyView,
    CategoryListView,
    JournalEntryByCategoryView,
)

urlpatterns = [
    path('entries/', JournalEntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', JournalEntryRetrieveUpdateDestroyView.as_view(), name='entry-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('entries/category/<int:category_id>/', JournalEntryByCategoryView.as_view(), name='entry-by-category'),
]