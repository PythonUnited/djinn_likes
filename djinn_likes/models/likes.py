from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.registry import CTRegistry
from django.contrib.auth.models import User


class Like(models.Model):

    """
    A user can like a content item once.
    """

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type',
                                                   'object_id')
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):

        return u"%d" % self.id

    class Meta:
        app_label = 'djinn_likes'
        ordering = ('-created', )


CTRegistry.register("like",
                    {"class": Like,
                     "app": "djinn_announcements",
                     "label": _("Like"),
                     "global_add": False,
                     "add_permission": "djinn_likes.add_like",
                     "filter_label": _("Like"),
                     "name_plural": _("Likes")})
