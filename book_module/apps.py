from django.apps import AppConfig


class BookModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_module'
    verbose_name = 'مدیریت کتاب ها'