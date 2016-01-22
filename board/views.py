#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.auth.models import User

from board.models import Board, Document
from core import utils


def test(request):
    result = '<html><body>'
    user = User.objects.create(username=utils.random_generator(16))
    board = Board.objects.create(user, "boardName", "boardDescription")
    result += str(board)

    for x in range(10):
        item = Document()
        item.board = board
        item.title = utils.random_generator(8)
        item.content = "hello content" + str(x)
        item.save()

    for i in board.item_set.all():
        result += str(i) + '\n'
        result += str(i.document)

    result += '</body></html>'

    return HttpResponse(result)
