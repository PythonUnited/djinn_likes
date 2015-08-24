
def likes_enabled(obj, request=None):

    if not hasattr(obj.__class__, 'likes'):
        return False

    return True
