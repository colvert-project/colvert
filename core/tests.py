from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AuthenticationViewsTests(TestCase):
    def setUp(self):
        self.user_password = "P@ssw0rd!"
        create_kwargs = {"username": "integration-user", "password": self.user_password}
        self.user = get_user_model().objects.create_user(**create_kwargs)

    def test_signin_page_renders(self):
        response = self.client.get(reverse("signin"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in")
        self.assertContains(response, 'id="signin-form"')

    def test_dashboards_requires_authentication(self):
        response = self.client.get(reverse("dashboards"))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("signin")))

    def test_signin_post_authenticates_and_redirects(self):
        response = self.client.post(
            reverse("signin"),
            {
                "username": self.user.username,
                "password": self.user_password,
            },
        )

        self.assertRedirects(response, reverse("dashboards"))

    def test_signin_api_returns_json_error_for_invalid_credentials(self):
        response = self.client.post(
            reverse("signin_api"),
            {
                "username": self.user.username,
                "password": "wrong-password",
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json()["success"])

    def test_signin_api_authenticates_and_returns_redirect_url(self):
        response = self.client.post(
            reverse("signin_api"),
            {
                "username": self.user.username,
                "password": self.user_password,
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.json()["redirect_url"], reverse("dashboards"))

    def test_signout_api_clears_authenticated_session(self):
        login_kwargs = {"username": self.user.username, "password": self.user_password}
        self.client.login(**login_kwargs)

        response = self.client.post(
            reverse("signout_api"),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["redirect_url"], reverse("signin"))
        dashboard_response = self.client.get(reverse("dashboards"))
        self.assertEqual(dashboard_response.status_code, 302)
