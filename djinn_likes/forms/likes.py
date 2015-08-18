from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.forms.base import BaseForm
from djinn_likes.models.likes import Like


class LikeForm(BaseForm):

    @property
    def labels(self):

        return {'submit': _('Save like'),
                'cancel': _('Cancel'),
                'header': _('Add like')}

    class Meta(BaseForm.Meta):
        model = Like
        fields = ('content_type', 'object_id', 'user')
