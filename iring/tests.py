#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import Collection, DocumentItem, Item
from django.contrib.auth.models import User


class BoardTestCase(TestCase):
    def testBoardCRUD(self):
        pass


class ItemTestCase(TestCase):
    def testItemCRUD(self):
        user = User.objects.create(username="u1")
        board = Collection.objects.create(user, "boardName", "boardDescription")
        print(board)

        for x in range(100):
            item = DocumentItem()
            item.board = board
            item.title = "title"
            item.content = "hello content"
            item.save()

        # for i in board.item_set.all():
        for i in Item.objects.all():
            print(i)

        for i in DocumentItem.objects.all():
            print(i)
