from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ(question="What is Django?", answer="Django is a web framework.")
        faq.save()
        self.assertEqual(faq.get_translated_question('hi'), faq.question_hi)