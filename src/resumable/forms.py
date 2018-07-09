from django import forms
from django.conf import settings

from .fields import ResumableFileField


class ResumableForm(forms.Form):
    file = ResumableFileField(
        allowed_mimes=("application/zip",),
        upload_url="/resumable/upload/",
        chunks_dir=getattr(settings, 'FILE_UPLOAD_TEMP_DIR')
    )