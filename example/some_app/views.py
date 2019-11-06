from django.views.generic import TemplateView

__all__ = (
    'SomePageView',
)


class SomePageView(TemplateView):
    template_name = 'index.jinja'