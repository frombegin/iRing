#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from iring.models import Collection, DocumentItem


def test(request):

    result = ''
    user = User.objects.create(username="fsfafs")
    board = Collection.objects.create(user, "boardName", "boardDescription")
    result += str(board)

    for x in range(100):
        item = DocumentItem()
        item.board = board
        item.title = "title"
        item.content = "hello content"
        item.save()

    # for i in board.documentitem_set.all():
    #     result += str(i) + '\n'

    return result
