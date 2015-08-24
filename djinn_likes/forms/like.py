from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_likes.models.likes import Like


class LikeForm(forms.Form):

    @property
    def labels(self):

        return {'submit': _('Save like'),
                'cancel': _('Cancel'),
                'header': _('Add like')}

    class Meta:
        model = Like
        fields = ('content_type', 'object_id', 'user')
