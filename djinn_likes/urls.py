from django.conf.urls import patterns, url, include
from djinn_contenttypes.views.utils import generate_model_urls
#from models import
from views.like import ToggleLikeView, LikersForObject


_urlpatterns = patterns(
    "",

    # # Viewlet
    # url(r"^$",
    #     AnnouncementViewlet.as_view(),
    #     name="djinn_announcements"),
    #
    # url(r"^priority$",
    #     PriorityAnnouncementViewlet.as_view(),
    #     name="djinn_priority_announcements"),
    #
    url(r"^toggle",
        ToggleLikeView.as_view(),
        name="djinn_toggle_like"),

    url(r"^likes",
        LikersForObject.as_view(),
        name="djinn_likes_for_object"),


    )

urlpatterns = patterns(
    '',

    (r'^djinn_likes/', include(_urlpatterns)),
    # (r'^announcements/', include(generate_model_urls(Announcement))),
    # (r'^announcements/', include(generate_model_urls(ServiceAnnouncement))),
    # (r'^announcements/', include(generate_model_urls(AnnouncementUpdate))),
)
