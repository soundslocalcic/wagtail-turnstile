from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings
from turnstile.utils import verify_turnstile_response
from unittest.mock import patch


class TurnstileUtilsTests(TestCase):
    def test_missing_secret_key(self):
        with self.assertRaises(ImproperlyConfigured):
            verify_turnstile_response("valid-token")

    @override_settings(TURNSTILE_SITE_KEY="test_site")
    @override_settings(TURNSTILE_SECRET_KEY="test_secret")
    @patch("turnstile.utils.requests.post")
    def test_successful_verification_returns_true(self, mock_post):
        mock_post.return_value.json.return_value = {
            "success": True
        }

        self.assertTrue(
            verify_turnstile_response("valid-token")
        )

        mock_post.assert_called_once()

    @override_settings(TURNSTILE_SITE_KEY="test_site")
    @override_settings(TURNSTILE_SECRET_KEY="test_secret")
    @patch("turnstile.utils.requests.post")
    def test_failed_verification_returns_false(self, mock_post):
        mock_post.return_value.json.return_value = {
            "success": False
        }

        self.assertFalse(
            verify_turnstile_response("bad-token")
        )
