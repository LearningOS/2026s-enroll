import unittest
from template_support.check_config import validate


class TemplateConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.config = {'prefix': '2026s-rcore'}
        self.env = {'STUDENT_GITHUB': 'Student-123', 'GITHUB_REPOSITORY': 'LearningOS/preparing-2026s-rcore-Student-123',
                    'COURSE_ID': '123', 'COURSE_TOKEN': 'test-only', 'COURSE_API_URL': 'https://api.opencamp.cn/web/api/courseRank/createByThirdToken'}

    def test_preparing_and_published_repositories_match(self):
        self.assertEqual(validate(self.config, self.env), 'Student-123')
        self.env['GITHUB_REPOSITORY'] = 'LearningOS/2026s-rcore-Student-123'
        self.assertEqual(validate(self.config, self.env), 'Student-123')

    def test_wrong_course_owner_or_identity_is_rejected(self):
        for repository in ['Other/2026s-rcore-Student-123', 'LearningOS/2026a-rcore-Student-123', 'LearningOS/2026s-rcore-Other']:
            with self.subTest(repository=repository), self.assertRaises(ValueError):
                validate(self.config, {**self.env, 'GITHUB_REPOSITORY': repository})

    def test_missing_or_invalid_credentials_fail_without_exposing_values(self):
        for key, value in [('COURSE_ID', ''), ('COURSE_ID', '0'), ('COURSE_ID', 'invalid'), ('COURSE_TOKEN', ''), ('COURSE_API_URL', 'https://example.com')]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate(self.config, {**self.env, key: value})
