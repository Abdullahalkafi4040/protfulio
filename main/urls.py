from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from baseapp.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)