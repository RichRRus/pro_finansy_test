from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название')

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return f'Голосование {self.title}'


class PollOption(models.Model):
    option = models.TextField(verbose_name='Вариант ответа')
    poll = models.ForeignKey('poll.Poll', on_delete=models.CASCADE, related_name='options', verbose_name='Голосование')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return f'Вариант ответа {self.option[:10]} к голосованию #{self.poll.pk}'


class PollAnswer(models.Model):
    option = models.ForeignKey(
        'poll.PollOption', on_delete=models.RESTRICT, related_name='answers', verbose_name='Ответ'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'Ответ {self.option.option[:10]} в голосовании #{self.option.poll.pk}'
