from django.conf import settings
from django.core.urlresolvers import reverse

from resumable.fields import ResumableFileField


class ResumableForm(Form):
    file = ResumableFileField(
        allowed_mimes=("audio/ogg",),
        upload_url=lambda: reverse('upload'),
        chunks_dir=getattr(settings, 'FILE_UPLOAD_TEMP_DIR')
    )