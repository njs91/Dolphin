from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messages'
    # label required, otherwise duplicate naming issue with INSTALLED_APPS
    label = 'email_messages'
