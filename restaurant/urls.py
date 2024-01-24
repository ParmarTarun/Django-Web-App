from django.urls import path
from .views import MenuItemsView, index, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    # path('about/', views.about, name='about'),
    path('items/', MenuItemsView.as_view()),
    path('<int:pk>/', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
