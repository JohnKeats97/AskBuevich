from ask_buevich.models import Question
from django import template

register = template.Library()

@register.inclusion_tag('Modules/best_questions.html')
def best_questions():
    choices = Question.objects.best_questions()
    choices = choices[:5]
    return {'choices': choices}
