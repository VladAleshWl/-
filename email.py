from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.text import MIMEText


settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


def send(list_to, subject, body, file=False):

    msg = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        bcc=list_to,
        headers={'From': settings.DEFAULT_FROM_EMAIL}
    )
    if file:
        for f in file:  # add files to the message
            msg.attach(f.name, f.file.read(), f.content_type)

    msg.content_subtype = 'html'

    msg.send()


def render_html(template, variables):
    # plaintext_context = Context(autoescape=False)
    return render_to_string(template, variables)  # , plaintext_context)

