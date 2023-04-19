from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),    #product:list
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),    #product:detail
    path('add/', views.ProductCreateView.as_view(), name='add'),    #product:add
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),    #product:edit
    path('remove/<int:pk>/', views.ProductDeleteView.as_view(), name='remove'),    #product:remove
]