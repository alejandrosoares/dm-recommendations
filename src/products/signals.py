from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from utils.cache.recommendations import delete_all_cache_recommendations
from .models import Product


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, **kwargs):
    delete_all_cache_recommendations()


@receiver(post_delete, sender=Product)
def post_delete_product(sender, instance, **kwargs):
    delete_all_cache_recommendations()
