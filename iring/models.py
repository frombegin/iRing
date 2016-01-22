#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from core.models import TimestampedModel


class CollectionManager(models.Manager):
    def create(self, user, name, description):
        return super().create(user=user, name=name, description=description)


class Collection(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120)
    description = models.TextField()
    objects = CollectionManager()

    def __str__(self):
        return "board[{}]: {} {}".format(self.id, self.name, self.description)


class Item(TimestampedModel):
    board = models.ForeignKey(Collection)
    title = models.CharField(max_length=120)

    def __str__(self):
        return "Item{}".format(self.simhash)


class DocumentItem(Item):
    content = models.TextField()
    simhash = models.CharField(max_length=16)

    def __str__(self):
        return "Document[{}]: {}, {}".format(self.id, self.title, self.content)


class AbstractFileItem(Item):
    name = models.CharField(max_length=128)
    size = models.BigIntegerField()
    sha1 = models.CharField(max_length=20)

    class Meta:
        abstract = True


class FileItem(AbstractFileItem):
    pass


class ImageItem(AbstractFileItem):
    width = models.IntegerField()
    height = models.IntegerField()


class Follower(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    collection = models.ForeignKey(Collection)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
