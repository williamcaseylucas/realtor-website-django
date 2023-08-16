from django.apps import AppConfig

# Add this to django config
class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
