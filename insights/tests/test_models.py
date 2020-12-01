from django.test import TestCase
from insights.models import Insight,InsightsCategory
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.category1 = InsightsCategory.objects.create(
            title = 'Eye problems',                                    
        )

        self.category2 = InsightsCategory.objects.create(
            title = 'Pediatrics',
            
        )

        self.user = self.setup_user()
        self.user.save()
        
        
        self.inquiry = Insight.objects.create(
            title = "I am having serious eye problems",
            slug ="eye-problem",
            user = self.user,
            category = self.category1,            
            body = "Some details",
            postImage="",
            
        )
        
    @staticmethod
    def setup_user():
        
        return User.objects.create_user(
            first_name ='test',
            last_name = 'testsur',
            email='testuser@test.com',
            username = 'myusername',
            password='test',
        )

    def test_get_category_name(self):
        self.assertEquals(self.category1.title, 'Eye problems')
        self.assertEquals(self.category2.title, 'Pediatrics')

        
    def test_get_inquiry_category(self):
        self.assertEquals(self.inquiry.category.title, 'Eye problems')

