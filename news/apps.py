from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Модели'

# class PortfolioConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'portfolio'
#     verbose_name = 'Портфолио'
