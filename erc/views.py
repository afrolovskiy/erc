from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'index.html'


class FeedbackView(TemplateView):
	template_name = 'feedback.html'


class ServicesView(TemplateView):
	template_name = 'services.html'


class ContactsView(TemplateView):
	template_name = 'contacts.html'
