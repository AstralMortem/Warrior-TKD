from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/',include('account.urls')),
    path('api/news/',include('news.urls')),
    # path('api/gyms/',include('gyms.urls')),
    # path('api/events/',include('events.urls')),
    # path('api/main-page/',MainPageView.as_view(), name='main-page')

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] 

if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

