from django.contrib.auth.models import User
from djinn_likes.models import Like


class LikeableMixin(object):

    @property
    def likes(self):

        return Like.objects.filter(content_type=self.ct_class,
                                   object_id=self.id)

    def likers(self):

        return User.objects.filter(like__content_type=self.ct_class,
                                   like__object_id=self.id)

    def likes_count(self):

        return self.likes.count()

    def is_liked_by(self, user):

        return self.likes.filter(user=user).exists()

