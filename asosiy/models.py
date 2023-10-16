from django.db import models

JINS = [('Erkak', 'Erkak'), ('Ayol', 'Ayol')]


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    kurs = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(choices=JINS, max_length=6)
    tugilgan_sana = models.DateField(verbose_name="Tug'ilgan sana: ")
    kitoblar_soni = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE, related_name='kitoblari')

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=255)

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateField()

