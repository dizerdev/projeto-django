from django.urls import path


from . import views

app_name = 'ecommerce'


urlpatterns = [
    path('', views.home, name="home"),
    path('product/<int:id>/', views.product, name="details"),
]
