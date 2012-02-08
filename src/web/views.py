
from django.contrib import messages
from django.views.generic import TemplateView

from contact_form.views import ContactFormView
from web.forms import ContactForm

class IndexView(TemplateView):
    template_name="web/index.html"


class Contact(ContactFormView):
    template_name = "web/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        response = super(Contact, self).form_valid(form)
        messages.success(self.request, "Thanks, your message was sent successfully!")
        return response

    def get_success_url(self):
        return self.request.path
