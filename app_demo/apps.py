from django.apps import AppConfig



class AppDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_demo'
    def ready(self):
        from app_demo import signals
    
        
    