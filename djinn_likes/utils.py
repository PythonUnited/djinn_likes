
def likes_enabled(obj, request):

    if not hasattr(obj.__class__, 'likes'):
        return False

    return True
