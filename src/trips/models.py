from django.db import models
from django.utils.translation import ugettext_lazy as _


class Trip(models.Model):

    class Classification(models.IntegerChoices):
        WORK = 1, _('work')
        PHYSICAL_ACTIVITY = 2, _('physical activity')
        RECREATION = 3, _('recreation')
        DISPLACEMENT = 4, _('displacement')


    customer = models.ForeignKey(
        'accounts.Customer',
        related_name='trips',
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(
        _('start date')
    )
    end_date = models.DateTimeField(
        _('end date')
    )
    rating = models.PositiveIntegerField(
        _('rating'),
        blank=True,
        null=True
    )
    classification = models.IntegerField(
        _('classification'),
        choices=Classification.choices,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')

    def __str__(self):
        return self.customer.name
