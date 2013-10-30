from django.contrib.auth.models import User

from lettuce import step
from lettuce.django.steps.models import (creates_models,
                                         hashes_data,
                                         reset_sequence)


@creates_models(User)
def create_user(step):
    """
    Create users setting the password
    """

    data = hashes_data(step)

    for hash_ in data:
        is_superuser = hash_.pop('is_superuser', False)

        if is_superuser:
            user = User.objects.create_superuser(**hash_)
        else:
            user = User.objects.create_user(**hash_)

        user.save()

    reset_sequence(User)
