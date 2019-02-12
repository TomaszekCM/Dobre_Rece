# from django.contrib.auth.models import User
# from django.db import models
#
# # Create your models here.
#
#
# class UserExtention(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE())
#     all_bags = models.IntegerField(default=0)
#     helped_orgs = models.IntegerField(default=0)
#     organised_collections = models.IntegerField(default=0)
#     type = models.CharField(choices=('osoba fizyczna', 'fundacja', 'organizacja pozarządowoa'))
#     password_reset_code = models.TextField()
#
#
# class Organisations(models.Model):
#     name = models.CharField(max_length=255)
#     mission = models.TextField()
#     type = models.CharField(choices=('fundacja', 'organizacja pozarządowoa'))
#     localisation = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#
#
# class OrganisationBeneficiaries(models.Model):
#     organisation = models.ManyToManyField(Organisations)
#     tag = models.CharField(max_length=255)
#
#
# # model where organisation can say what do they need
# class OrganisationArticles(models.Model):
#     organisation = models.ManyToManyField(Organisations)
#     article = models.CharField(max_length=255)
#
#
# # model for collections organised by someone ("wee need something for someone")
# class Collection(models.Model):
#     place = models.CharField(max_length=255)
#     goal = models.CharField(max_length=255)
#     date = models.DateTimeField()
#     description = models.TextField()
#     picture = models.FileField()
#
#
# class CollectionArticles(models.Model):
#     collection = models.ForeignKey(Collection, on_delete = models.CASCADE())
#     article = models.CharField(max_length=255)
#
#
# # model for spontaneous donations ("I have some redundant stuff, so I can give it to someone who may need it")
# class Donation(models.Model):
#     numb_of_bags = models.IntegerField()
#     beneficiary_city = models.CharField(max_length=255)
#     organisation = models.ManyToManyField(Organisations, null=True)
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     post_code = models.CharField(max_length=6)
#     phone = models.CharField(max_length=20)
#     date = models.DateField()
#     time = models.TimeField
#     additional_info = models.TextField()
#
#
# class DonationBeneficiaries(models.Model):
#     donation = models.ManyToManyField(Donation)
#     beneficiary = models.CharField(max_length=255)
#
#
# class DonationArticles(models.Model):
#     donation = models.ManyToManyField(Donation)
#     article = models.CharField(max_length=255)
