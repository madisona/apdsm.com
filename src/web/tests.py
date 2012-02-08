
from django import test
from django.core.urlresolvers import reverse

class AcceptanceTests(test.TestCase):

    def test_hits_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "web/index.html")

    def test_hits_services_page(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "web/services.html")

    def test_hits_rates_page(self):
        response = self.client.get(reverse("rates"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "web/rates.html")

    def test_hits_contact_page(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "web/contact.html")
