from django.db import transaction

from poll import models


class PollService:

    @staticmethod
    def create(**data: dict) -> models.Poll:
        options = data.pop('options', None)
        poll = models.Poll(**data)
        [option.update({'poll': poll}) for option in options]
        with transaction.atomic():
            poll.save()
            models.PollOption.objects.bulk_create(
                models.PollOption(**poll_option_data)
                for poll_option_data in options
            )
        return poll
