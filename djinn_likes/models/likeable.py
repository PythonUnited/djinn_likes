from djinn_likes.models import Like


class LikeableMixin(object):

    def likes(self):

        return Like.objects.filter(content_type=self.ct_class,
                                   object_id=self.id)

    def likes_count(self):

        return self.likes().count()

    def is_liked_by(self, user):

        return self.likes.filter(user=user).exists()

