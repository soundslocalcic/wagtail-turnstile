from django.template import Library
from django.utils.safestring import mark_safe


register = Library()


@register.simple_tag()
def turnstile_script():
    src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"  # NOQA
    return mark_safe('<script src="%s" async defer></script>' % src)
