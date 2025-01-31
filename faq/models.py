from .utils import translate_text
from ckeditor.fields import RichTextField
from django.db import models

def save(self, *args, **kwargs):
    if not self.question_hi:
        self.question_hi = translate_text(self.question, 'hi')
    if not self.answer_hi:
        self.answer_hi = translate_text(self.answer, 'hi')
    super().save(*args, **kwargs)


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question