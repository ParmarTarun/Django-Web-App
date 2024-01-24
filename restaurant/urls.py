from django.urls import path
from .views import MenuItemsView, index, SingleMenuItemView

urlpatterns = [
    path('', index, name='index'),
    # path('about/', views.about, name='about'),
    path('items/', MenuItemsView.as_view()),
    path('<int:pk>/', SingleMenuItemView.as_view()),
]
