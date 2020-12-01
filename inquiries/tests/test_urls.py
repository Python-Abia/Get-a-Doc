from django.test import SimpleTestCase
from django.urls import reverse, resolve
from inquiries.views import inquiries_list, inquiry_list, category_list, categories_list,syptoms_list, syptom_list

class TestUrls(SimpleTestCase):

    def test_inquiry_list_url_resolves(self):
        url = reverse('inquiries:inquiry_list',  args = ['1'])        
        self.assertEquals(resolve(url).func, inquiry_list)

    def test_inquiries_list_url_resolves(self):
        url = reverse('inquiries:inquiries_list')
        self.assertEquals(resolve(url).func, inquiries_list)


    def test_category_list_url_resolves(self):
        url = reverse('inquiries:category_list',  args = ['1'])
        self.assertEquals(resolve(url).func, category_list)


    def test_categories_url_resolves(self):
        url = reverse('inquiries:categories_list')
        self.assertEquals(resolve(url).func, categories_list)
        
    
    def test_syptoms_list_url_resolves(self):
        url = reverse('inquiries:category_list',  args = ['1'])
        self.assertEquals(resolve(url).func, category_list)


    def test_syptom_list_resolves(self):
        url = reverse('inquiries:categories_list')
        self.assertEquals(resolve(url).func, categories_list)
    
    
