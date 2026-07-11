from django.template import Library


register = Library()


@register.inclusion_tag("turnstile/turnstile_script.html")
def turnstile_script():
    return {}
