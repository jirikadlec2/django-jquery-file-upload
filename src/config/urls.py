from django.urls import include, path
from django.http import HttpResponseRedirect
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from resumable.views import ResumableUploadView
from resumable.views import resumable_demo
from resumable.views import demo
from resumable.views import fake_upload

urlpatterns = [
    path('', lambda x: HttpResponseRedirect('/upload/new/')),
    path('resumable/upload/', ResumableUploadView.as_view()),
    path("resumable_demo/", resumable_demo),
    path("demo/", demo),
    path("fake_upload/", fake_upload),
    path('upload/', include('fileupload.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
