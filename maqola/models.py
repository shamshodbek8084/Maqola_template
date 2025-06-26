from django.db import models

# Create your models here.

class Maqola(models.Model):

    talaba_fish = models.CharField(max_length=256)
    fakultet = models.TextField(max_length=256)
    fakultet_raqami = models.PositiveIntegerField()
    guruh_raqami = models.CharField(max_length=256)
    

    STATUS_MAQOLA = (
        ('Elektron', 'Elektron'),
        ('Bosma', 'Bosma'),
        ('Qo`l yozma', 'Qo`l yozma'),
    )

    number = models.PositiveIntegerField()
    title = models.CharField(max_length=256)
    format = models.CharField(max_length=56, choices=STATUS_MAQOLA, default='Elektron')

    publication_type = models.CharField(max_length=256)
    journal_name = models.CharField(max_length=256)
    volume = models.PositiveIntegerField()
    issue = models.PositiveIntegerField()
    published_date = models.DateTimeField()
    pages = models.CharField(max_length=56)

    bet_soni = models.PositiveIntegerField()
    mualliflar_soni = models.PositiveIntegerField()

    piece = models.CharField(max_length=256)

    authors = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.number}. {self.title}"
    
    @property
    def journal_information(self):
        return f'{self.publication_type} of collection, "{self.journal_name}", Volume - {self.volume}, Issue - {self.issue}, {self.published_date}, -B. {self.pages}'
    
    def save(self, *args, **kwargs):
        if self.bet_soni and self.mualliflar_soni:
            self.piece = f"{self.bet_soni}/{self.mualliflar_soni}"
        super().save(*args, **kwargs)





