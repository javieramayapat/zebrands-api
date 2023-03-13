import os

from django.core.mail import send_mail
from dotenv import load_dotenv

from users.models import User

load_dotenv()


def send_price_update_notification(product):
    admin_emails = User.objects.filter(is_staff=True).values_list('email', flat=True)

    subject = '🛒 Actualización de precio 🛒'
    message = f"El precio del producto {product.name} ha sido actualizado a ${product.price}." \
              f" \n\n Gracias por su atención \n\n Saludos 👋"
    email_verified = os.getenv('AWS_SES_EMAIL_VERIFIED')
    send_mail(
        subject,
        message,
        email_verified,
        admin_emails,
        fail_silently=False,
    )
