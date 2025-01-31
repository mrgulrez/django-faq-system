from django.db import models
from ckeditor.fields import RichTextField
from .utils import translate_text

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  
    question_bn = models.TextField(blank=True, null=True) 
    answer_hi = RichTextField(blank=True, null=True)  
    answer_bn = RichTextField(blank=True, null=True) 

    def save(self, *args, **kwargs):

        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')


        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question