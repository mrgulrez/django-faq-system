import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
class TestFAQModel:
    def test_faq_creation(self):
        """
        Test that an FAQ can be created and saved to the database.
        """
        faq = FAQ(
            question="What is Django?",
            answer="Django is a web framework."
        )
        faq.save()

        assert faq.id is not None
        assert faq.question == "What is Django?"
        assert faq.answer == "Django is a web framework."

    def test_translation_logic(self):
        """
        Test that translations are automatically generated during FAQ creation.
        """
        faq = FAQ(
            question="What is Django?",
            answer="Django is a web framework."
        )
        faq.save()

        # Check if Hindi translations are generated
        assert faq.question_hi is not None
        assert faq.answer_hi is not None

        # Check if Bengali translations are generated
        assert faq.question_bn is not None
        assert faq.answer_bn is not None

    def test_get_translated_question(self):
        """
        Test the get_translated_question method.
        """
        faq = FAQ(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डजांगो क्या है?",
            question_bn="ডjango কি?"
        )
        faq.save()

        # Test English (default)
        assert faq.get_translated_question() == "What is Django?"

        # Test Hindi
        assert faq.get_translated_question('hi') == "डजांगो क्या है?"

        # Test Bengali
        assert faq.get_translated_question('bn') == "ডjango কি?"

    def test_get_translated_answer(self):
        """
        Test the get_translated_answer method.
        """
        faq = FAQ(
            question="What is Django?",
            answer="Django is a web framework.",
            answer_hi="डजांगो एक वेब फ्रेमवर्क है।",
            answer_bn="ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"
        )
        faq.save()

        # Test English (default)
        assert faq.get_translated_answer() == "Django is a web framework."

        # Test Hindi
        assert faq.get_translated_answer('hi') == "डजांगो एक वेब फ्रेमवर्क है।"

        # Test Bengali
        assert faq.get_translated_answer('bn') == "ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"


@pytest.mark.django_db
class TestFAQAPI:
    def setup_method(self):
        """
        Set up test data for API tests.
        """
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डजांगो क्या है?",
            answer_hi="डजांगो एक वेब फ्रेमवर्क है।",
            question_bn="ডjango কি?",
            answer_bn="ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_fetch_faqs_in_english(self):
        """
        Test fetching FAQs in English (default).
        """
        url = reverse('faq-list')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data[0]['question'] == "What is Django?"
        assert response.data[0]['answer'] == "Django is a web framework."

    def test_fetch_faqs_in_hindi(self):
        """
        Test fetching FAQs in Hindi.
        """
        url = reverse('faq-list')
        response = self.client.get(url, {'lang': 'hi'})
        assert response.status_code == 200
        assert response.data[0]['question'] == "डजांगो क्या है?"
        assert response.data[0]['answer'] == "डजांगो एक वेब फ्रेमवर्क है।"

    def test_fetch_faqs_in_bengali(self):
        """
        Test fetching FAQs in Bengali.
        """
        url = reverse('faq-list')
        response = self.client.get(url, {'lang': 'bn'})
        assert response.status_code == 200
        assert response.data[0]['question'] == "ডjango কি?"
        assert response.data[0]['answer'] == "ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"