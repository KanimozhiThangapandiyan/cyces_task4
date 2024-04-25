from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.cms.models import DashBoard,JobPosting

@receiver(post_save, sender=JobPosting)
@receiver(post_delete, sender=JobPosting)
def update_model_count(sender, instance, **kwargs):
    model_name = sender.__name__  # Get the name of the model
    count = JobPosting.objects.count()  # Get the count of objects
    # Update or create the ModelCount instance
    DashBoard.objects.update_or_create(model_name=model_name, defaults={'count': count})
