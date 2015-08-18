from django.conf.urls import patterns, url, include
from djinn_contenttypes.views.utils import generate_model_urls
#from models import


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
    # url(r"^service$",
    #     ServiceAnnouncementViewlet.as_view(),
    #     name="djinn_service_announcements"),
    #
    )

urlpatterns = patterns(
    '',

    (r'^announcements/', include(_urlpatterns)),
    # (r'^announcements/', include(generate_model_urls(Announcement))),
    # (r'^announcements/', include(generate_model_urls(ServiceAnnouncement))),
    # (r'^announcements/', include(generate_model_urls(AnnouncementUpdate))),
)
