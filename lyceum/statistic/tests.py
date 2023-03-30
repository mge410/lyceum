from django.test import Client
from django.test import TestCase

import catalog.models
import rating.models
import users.models


class StatsTests(TestCase):
    user_register_data = {
        'username': 'ABEBRA',
        'email': 'aboba@ma.ru',
        'password1': '123123123g',
        'password2': '123123123g',
    }

    def setUp(self) -> None:
        self.test_user_with_review = (
            users.models.UserProfileProxy.objects.create_user(
                username=self.user_register_data['username']
            )
        )
        self.test_user_without_review = (
            users.models.UserProfileProxy.objects.create_user(
                username=''.join(
                    [
                        self.user_register_data['username'],
                        '_no_review',
                    ]
                )
            )
        )
        self.base_category = catalog.models.Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        self.base_tag = catalog.models.Tag.objects.create(
            name='Тестовый тэг',
            slug='test-tag-slug',
        )
        self.test_item = catalog.models.Item.objects.create(
            name='Тестовый товар',
            category=self.base_category,
            text='превосходно',
        )
        self.grade = rating.models.Grade.objects.create(
            user=self.test_user_with_review,
            item=self.test_item,
        )

    def test_user_stats_status_code_with_review(self) -> None:
        user_id = self.test_user_with_review.id
        response = Client().get(f'/statistic/{user_id}')
        self.assertTemplateUsed(response, 'statistic/user_statistic.html')
        self.assertEquals(response.status_code, 200)

    def test_user_stats_status_code_without_review(self) -> None:
        user_id = self.test_user_without_review.id
        response = Client().get(f'/statistic/{user_id}')
        self.assertTemplateUsed(response, 'statistic/user_statistic.html')
        self.assertEquals(response.status_code, 200)

    def test_user_stats_context_success(self) -> None:
        user_id = self.test_user_with_review.id
        response = Client().get(f'/statistic/{user_id}')
        context = response.context
        self.assertEquals(1, context.get('is_successful'))

    def test_user_stats_context_failure(self) -> None:
        user_id = self.test_user_without_review.id
        response = Client().get(f'/statistic/{user_id}')
        context = response.context
        self.assertEquals(0, context.get('is_successful'))

    def tearDown(self) -> None:
        catalog.models.Item.objects.all().delete()
        catalog.models.Tag.objects.all().delete()
        catalog.models.Category.objects.all().delete()
        users.models.User.objects.all().delete()
        rating.models.Grade.objects.all().delete()
        super(StatsTests, self).tearDown()
