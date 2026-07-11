from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings
from turnstile.widgets import TurnstileWidget


class TurnstileWidgetTests(TestCase):
    def test_missing_site_key(self):
        widget = TurnstileWidget()

        with self.assertRaises(ImproperlyConfigured):
            widget.render("turnstile", None)

    @override_settings(TURNSTILE_SITE_KEY="test_site")
    def test_widget_renders_correct_html(self):
        widget = TurnstileWidget()
        html = widget.render("turnstile", None)
        self.assertIn("turnstile.ready", html)
