from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


from erc.forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'index.html'


class FeedbackView(FormView):
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.send_email()
        return super(FeedbackView, self).form_valid(form)


class ServicesView(TemplateView):
    template_name = 'services.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'
