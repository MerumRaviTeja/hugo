"""attedance URL Configuration here

"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls import include, url
#from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .web.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/", include("attedance.api.urls")),
    path("", include("attedance.web.urls")),
    path("home/",home),
    path("check-in-page/",check_in_page),
    path("check-out-redirect/",check_out_redirect),
    path("check-out-page/",check_out_page),
    path("check-out/",check_out),
    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    url(r'^accounts/', include('allauth.urls')),


] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
