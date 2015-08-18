from django import template

# from likes.utils import can_vote, likes_enabled
from utils import likes_enabled

register = template.Library()

@register.inclusion_tag('djinn_likes/includes/likes_block.html', takes_context=True)
def likes(context, obj, template=None):
    if template is None:
        template = 'djinn_likes/includes/likes.html'

    request = context['request']

    context.update({
        'template': template,
        'content_obj': obj,
        'likes_enabled': likes_enabled(obj, request),
        'content_type': "-".join((obj._meta.app_label, obj._meta.module_name)),
    })
    return context