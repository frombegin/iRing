#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class CollectionManager(models.Manager):
    @staticmethod
    def create(user, name, description):
        board = Collection()
        board.user = user
        board.name = name
        board.description = description
        board.save()
        return board


class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CollectionManager()

    def __str__(self):
        return "board[{}]: {} {}".format(self.id, self.name, self.description)


class Item(models.Model):
    board = models.ForeignKey(Collection)
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DocumentItem(Item):
    content = models.TextField()

    def __str__(self):
        return "Document[{}]: {}, {}".format(self.id, self.title, self.content)


class FileItem(Item):
    size = models.BigIntegerField()


class ImageItem(Item):
    width = models.IntegerField()
    height = models.IntegerField()


class Follower(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    collection = models.ForeignKey(Collection)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
