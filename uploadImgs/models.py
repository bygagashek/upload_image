import uuid
from django.db import models
from django.core.exceptions import ValidationError
import os


class Pictures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def validate_image(picture):
        filesize = picture.size
        kilobyte_limit = 200
        if filesize > kilobyte_limit*1024:
            raise ValidationError("Failed to load images")

    def path_and_rename(path, prefix):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]

            if instance.pk:
                complaint_id = "cid_%s" % (instance.pk,)
                filename = '{}.{}.{}'.format(prefix, complaint_id, ext)
            else:

                random_id = "rid_%s" % (uuid4().hex,)
                filename = '{}.{}.{}'.format(prefix, random_id, ext)

            return os.path.join(path, filename)

        return wrapper

    picture = models.ImageField(upload_to=path_and_rename("complaint_files", 'picture'), max_length=500,
                                validators=[validate_image], help_text="Browse a file")
