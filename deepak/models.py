from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BloodRequest(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    hospital = models.CharField(max_length=150)
    needed_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'blood request'
        verbose_name_plural = 'blood requests'

    def __str__(self):
        return f'{self.blood_group} request for {self.full_name}'
