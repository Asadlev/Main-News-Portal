from django import template


register = template.Library()


@register.filter()
def currency(value, code):
    if len(code) not in 10:
        return f'{value}...'
    return 'note pad'

# Реализововаем фильтр, который заменяет нецензурные слова на "*"
@register.simple_tag(takes_context = True)
def disabling_obscene_words(value):
    words = value.split()
    forbidden_words = ['Тупой', 'Козел', 'Нецензурный']
    result = []
    for clean in words:
        if clean in forbidden_words:
            result.append(clean[0] + '*' * (len(clean)-2) + clean[-1])
        result.append(clean)
    return " ".join(result)

print(disabling_obscene_words('Тупой'))
