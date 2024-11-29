from django.urls import path
from WEBAPP import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name = "home"),
    path('services', views.services, name = "services"),
    path('shop', views.shop, name = "shop"),
    path('contact', views.contact, name = "contact"),
    path('blog', views.blog, name = "blog"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)