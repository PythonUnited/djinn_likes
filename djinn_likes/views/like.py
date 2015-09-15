from django.views.generic import TemplateView
from djinn_likes.models import Like
from djinn_likes.forms.like import LikeForm
from djinn_core.utils import urn_to_ctype_and_id, urn_to_object
from pgintranet.apps.pu_in_content.views.jsonbase import JSONFormView


class ToggleLikeView(JSONFormView):

    model = Like
    form_class = LikeForm
    template_name = "djinn_likes/includes/like_button.html"

    def form_valid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        self.object = urn_to_object(form.data.get('uri'))

        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):

        return self.form_valid(form)

    def get_context_data(self, **kwargs):

        context = super(ToggleLikeView, self).get_context_data(**kwargs)

        context['edit_mode'] = True

        context.update({'object': self.object,
                        'is_liked_by_user': self.object.is_liked_by(
                            self.request.user)
        })

        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)

        ctype, obj_id = urn_to_ctype_and_id(form.data.get('uri'))

        if ctype:
            like, created = Like.objects.get_or_create(
                user=request.user, content_type=ctype, object_id=obj_id)

            if not created:
                like.delete()

        response = super(ToggleLikeView, self).post(request, args, kwargs)

        return response


class LikersForObject(TemplateView):
    '''
    This view is called ajaxy by a callback from the 'like' button
    '''

    template_name = 'djinn_likes/likes.html'

    def get_context_data(self, **kwargs):

        ctx = super(LikersForObject, self).get_context_data(**kwargs)
        ctx['object'] =  urn_to_object(self.request.REQUEST['uri'])

        return ctx