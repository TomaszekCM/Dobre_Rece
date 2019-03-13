from django.contrib.auth.models import User
from django.db import models


class PersonDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    all_bags = models.IntegerField(default=0)
    helped_orgs = models.IntegerField(default=0)
    organised_collections = models.IntegerField(default=0)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    post_code = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=20, null=True)
    password_reset_code = models.TextField()


org_types = ((1, 'fundacja'), (2, 'organizacja pozarządowoa'))


class OrganisationDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mission = models.TextField()
    type = models.IntegerField(choices=org_types)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=20)
    helped_times = models.IntegerField(default=0)
    received_bags = models.IntegerField(default=0)
    password_reset_code = models.TextField()


class GlobalStatistics(models.Model):
    '''On the langing page, there has to be info about global statistics - it would be easier to display ready data,
    than to count it each time. So there is going to be only one object, edited as soon as someon makes some collection. etc '''
    numb_of_bags = models.IntegerField()
    helped_orgs = models.IntegerField()
    organised_collections = models.IntegerField()


class OrganisationBeneficiaries(models.Model):
    '''Who is going to benefit from the specific organisation - eg. 'children', 'homeless', etc.'''
    organisation = models.ManyToManyField(OrganisationDetails)
    tag = models.CharField(max_length=255)


class OrganisationArticles(models.Model):
    '''Organisation can specify what kind of articles they need - eg. 'blankets', 'food', etc.'''
    organisation = models.ManyToManyField(OrganisationDetails)
    article = models.CharField(max_length=255)


class Collection(models.Model):
    '''Model for collections organised by someone ("wee need something for someone")'''
    place = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    picture = models.FileField()
    who_organised = models.ForeignKey(User, on_delete=models.CASCADE)


class CollectionArticles(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    article = models.CharField(max_length=255)


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
