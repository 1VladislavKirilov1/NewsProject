from django import template

register = template.Library()


text = 'New Music Online'
x = text.split()


@register.filter()
def censor(text):
    t1 = text.split()
    f = text.replace('Music', 'M***c')
    for t in t1:
        if t in x:
            return f'{f}'
    else:
        return f'{text}'