# obituaries/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Obituary


class ObituaryModelTests(TestCase):

    def setUp(self):
        # Create a sample obituary for testing
        self.obituary = Obituary.objects.create(  # pylint: disable=no-member
            name="mansa musa",
            date_of_birth="1900-01-10",
            date_of_death="1990-10-12",
            content="our beloved king, leader and hero.",
            author="musa the II",
            slug="mansa-musa"
        )

    def test_obituary_creation(self):
        # Test if the obituary is created successfully
        self.assertEqual(self.obituary.name, "mansa musa")
        self.assertEqual(self.obituary.slug, "mansa-musa")


class ObituaryDetailViewTests(TestCase):

    def setUp(self):
        # Create a sample obituary for testing
        self.obituary = Obituary.objects.create(  # pylint: disable=no-member
            name="mansa musa",
            date_of_birth="1900-01-10",
            date_of_death="1990-10-12",
            content="our beloved king, leader and hero.",
            author="musa the II",
            slug="mansa-musa"
        )

    def test_obituary_detail_view(self):
        # Test if the detail view returns a 200 status code
        response = self.client.get(
            reverse('obituary_detail', args=[self.obituary.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.obituary.name)
        self.assertContains(response, self.obituary.content)
