from django.test import SimpleTestCase


class SmokeTest(SimpleTestCase):
    def test_django_settings_load(self):
        from django.conf import settings
        self.assertTrue(settings.configured)