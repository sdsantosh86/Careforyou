from django.db import models


class Childcare(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    provider_id = models.ForeignKey('Provider', on_delete=models.CASCADE)
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE)
    language_id = models.ForeignKey("Language", on_delete=models.CASCADE)
    type_id = models.ForeignKey('ChildcareType', on_delete=models.CASCADE)
    suburb_id = models.ForeignKey('Suburb', on_delete=models.CASCADE)
    state = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    fax = models.CharField(max_length=12, null=True)
    after_school = models.BooleanField(null=True)
    before_school = models.BooleanField(null=True)
    vacation = models.BooleanField(null=True)
    long_day_care = models.BooleanField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    temp_closed = models.BooleanField(null=True)


class Provider(models.Model):
    provider_id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)


class Program(models.Model):
    program_id = models.CharField(max_length=11, primary_key=True)
    type = models.CharField(max_length=20)


class Language(models.Model):
    language_id = models.CharField(max_length=11, primary_key=True)
    language = models.CharField(max_length=20)


class ChildcareType(models.Model):
    type_id = models.CharField(max_length=11, primary_key=True)
    type = models.CharField(max_length=11)


class Suburb(models.Model):
    suburb_id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=11)
    postcode = models.CharField(max_length=4)


class Quality(models.Model):
    quality_id = models.CharField(max_length=11, primary_key=True)
    childcare_id = models.ForeignKey("Childcare", on_delete=models.CASCADE, null=True)
    area1 = models.IntegerField()
    area2 = models.IntegerField()
    area3 = models.IntegerField()
    area4 = models.IntegerField()
    area5 = models.IntegerField()
    area6 = models.IntegerField()
    area7 = models.IntegerField()
    overall = models.IntegerField()
    issued_date = models.DateTimeField()


class OpeningHours(models.Model):
    opening_hours_id = models.CharField(max_length=11, primary_key=True)
    childcare_id = models.ForeignKey("Childcare", on_delete=models.CASCADE, null=True)
    mon_s = models.DateTimeField()
    mon_e = models.DateTimeField()
    tue_s = models.DateTimeField()
    tue_e = models.DateTimeField()
    wed_s = models.DateTimeField()
    wed_e = models.DateTimeField()
    thu_s = models.DateTimeField()
    thu_e = models.DateTimeField()
    fri_s = models.DateTimeField()
    fri_e = models.DateTimeField()
    sat_s = models.DateTimeField()
    sat_e = models.DateTimeField()
    sun_s = models.DateTimeField()
    sun_e = models.DateTimeField()
