from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('', include('Apps.Web.Website.urls')),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


