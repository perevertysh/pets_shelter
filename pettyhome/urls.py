from django.contrib import admin

from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.url import url
from django.views.generic.base import TemplateView

from rest_framework import routers

from pets.views import IndexPageView, home

from pets.urls import routes as pets_routes
from petdocs.urls import routes as petdocs_routes
from pets.urls import urlpatterns as pets_patterns

router = routers.DefaultRouter()
for route in (pets_routes
              + petdocs_routes):
    router.register(*route)

urlpatterns = [
    # path('', IndexPageView.as_view()),
    path('', home),
    # url(r'', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += pets_patterns
