from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test", password="test", email="test@email.com", port="LAGOS")

    def test_string_rep(self):
        self.assertEqual(str(self.user), "test@email.com")

    def test_signup(self):
        pass

    def test_login(self):
        pass

    def test_restriction(self):
        issue_create_test = self.client.get('/create/')
        dashboard_access_test = self.client.get('/dashboard/')

        self.assertEqual(issue_create_test.status_code, 302)
        self.assertEqual(
            issue_create_test.headers["location"], "/login?next=/create/")
        self.assertEqual(dashboard_access_test.status_code, 302)
        self.assertEqual(
            dashboard_access_test.headers["location"], "/login?next=/dashboard/")
