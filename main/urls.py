from django.urls import path
from main import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),

]