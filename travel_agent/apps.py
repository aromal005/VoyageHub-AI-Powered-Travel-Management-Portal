from django.apps import AppConfig
# from background_task.models import Task


class TravelAgentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travel_agent'

    def ready(self):
        # Import Task inside ready to avoid AppRegistryNotReady
        from background_task.models import Task
        from .tasks import pro_expiry_reminder

        task_name = "Pro Expiry Reminder"
        if not Task.objects.filter(verbose_name=task_name).exists():
            pro_expiry_reminder(schedule=0, repeat=60, verbose_name=task_name)