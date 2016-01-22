#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from core.models import TimestampedModel


class BoardManager(models.Manager):
    def create(self, user, name, description):
        return super().create(user=user, name=name, description=description)


class Board(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120)
    description = models.TextField()
    objects = BoardManager()

    def __str__(self):
        return "board[{}]: {} {}".format(self.id, self.name, self.description)


class Item(TimestampedModel):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=120)
    type_id = models.CharField(max_length=8)

    def __str__(self):
        return "Item{}".format(self.simhash)


class Document(Item):
    content = models.TextField()
    simhash = models.CharField(max_length=16)

    def __str__(self):
        return "Document[{}]: {}, {}".format(self.id, self.title, self.content)


class AbstractFileItem(Item):
    filename = models.CharField(max_length=128)
    size = models.BigIntegerField()
    sha1 = models.CharField(max_length=20)

    class Meta:
        abstract = True


class File(AbstractFileItem):
    description = models.TextField(max_length=255)


class Image(AbstractFileItem):
    width = models.IntegerField()
    height = models.IntegerField()
    mime = models.CharField(max_length=8)


class Follower(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    board = models.ForeignKey(Board)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
