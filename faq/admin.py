from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    fields = ('question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')