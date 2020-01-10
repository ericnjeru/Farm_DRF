from __future__ import unicode_literals
from django.conf import settings
import uuid
from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


def get_image_name(instance, filename):
    ext = filename.split('.')[-1]
    uid = uuid.uuid4().hex[:10]
    filename = "products/%s_%s.%s" % (instance.p_name, uid, ext)
    return filename


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p_name = models.CharField(_("Name"), max_length=255)
    p_category = models.CharField(_("Category"), max_length=255)
    p_price = models.CharField(_("Price"), max_length=255)
    p_price_unit = models.CharField(_("Unit Price"), max_length=255)
    p_description = models.CharField(_("Description"), max_length=255)
    p_image = models.ImageField(upload_to=get_image_name, blank=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __unicode__(self):
        return smart_unicode(self.p_name)
