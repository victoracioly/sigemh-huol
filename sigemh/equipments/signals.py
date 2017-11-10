from django.utils.text import slugify


def pre_save_equipment_type(sender, instance, *args, **kwargs):

    instance.slug = slugify(instance.name)
