from django import template

# from likes.utils import can_vote, likes_enabled
#from djinn_likes.utils import likes_enabled

register = template.Library()


def likes_enabled(obj, request=None):

    if not hasattr(obj.__class__, 'likes'):
        return False

    return True

@register.inclusion_tag('djinn_likes/includes/like_button.html', takes_context=True)
def like_button(context, obj):

    return {"is_liked_by_user": obj.is_liked_by(context['request'].user),
            "object": obj}

@register.inclusion_tag('djinn_likes/includes/likes_block.html', takes_context=True)
def likes(context, obj, template=None):
    if template is None:
        template = 'djinn_likes/includes/likes.html'

    request = context['request']

    context.update({
        'template': template,
        'liked_object': obj,
        'likes_enabled': likes_enabled(obj, request),
        'likes_content_type': "-".join((obj._meta.app_label, obj._meta.module_name)),
    })
    return context

@register.inclusion_tag('djinn_likes/includes/likers.html', takes_context=True)
def show_likers(context, obj):
    likers = obj.likers()

    likers_list = []
    user_likes_this = False

    if likers.filter(id=context['request'].user.id):
        likers_list.append(("Jij", context['request'].user.get_profile()))
        user_likes_this = True

    for liker in likers:
        if liker != context['request'].user:
            prfile = liker.get_profile()
            likers_list.append((unicode(prfile), prfile))

    num_names_longlist = 20

    return {"liked_object": obj,
            "likers_list": likers_list,
            "likers_count": len(likers_list),
            "user_likes_this": user_likes_this,
            "likers_long": likers_list[:num_names_longlist],
            "extra_likers": max(len(likers_list) - num_names_longlist, 0)
            }


