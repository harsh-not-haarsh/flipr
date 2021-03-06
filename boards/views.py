from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, List, Card
from django.http import HttpResponse
# from django.urls import


# from django.views.generic import CreateView


@login_required(login_url='/accounts/login')
def CreateBoard(request):
    if request.method == 'POST':
        board = Board.objects.create(name=request.POST.get('name'))
        board.members.add(request.user)
        board.admins.add(request.user)
        return redirect('/board/{}/display'.format(board.obj_id))
    return render(request, 'boards/create_board.html')


@login_required(login_url='/accounts/login')
def CreateList(request, obj_id):
    if request.method == 'POST':
        board = get_object_or_404(Board, obj_id=obj_id)
        list1 = List.objects.create(name=request.POST.get('name'))
        board.lists.add(list1)
        return Display(request, obj_id=obj_id)
    return render(request, 'boards/create_list.html')


@login_required(login_url='/accounts/login')
def CreateCard(request, obj_id):
    if request.method == 'POST':
        list1 = get_object_or_404(List, obj_id=obj_id)
        card = Card.objects.create(name=request.POST.get('name'))
        card.content = request.POST.get('content')
        card.due_date = request.POST.get('due_date')
        # card.file = request.POST.get('file')
        # card.link = request.POST.get('link')
        list1.cards.add(card)
        # card.save()
        return redirect("/board/{}/list".format(obj_id))

    return render(request, 'boards/create_card.html')


@login_required(login_url='/accounts/login')
def Display(request, obj_id="123"):
    board = get_object_or_404(Board, obj_id=obj_id)
    return render(request, 'boards/display.html', {'board': board})


@login_required(login_url='/accounts/login')
def DisplayList(request, obj_id):
    list1 = get_object_or_404(List, obj_id=obj_id)
    boards = list1.list.all()
    for x in boards:
        board = x
    return render(request, 'boards/list.html', {'board': board, 'list1': list1})


@login_required(login_url='/accounts/login')
def ShareBoard(request, obj_id):
    return HttpResponse("Share Board Id: <b>{}</b> with your team members.".format(obj_id))


@login_required(login_url='/accounts/login')
def JoinBoard(request):
    if request.method == 'POST':
        obj_id = request.POST.get('obj_id')
        board = get_object_or_404(Board, obj_id=obj_id)
        board.members.add(request.user)
        return redirect('/board/{}/display'.format(obj_id))
    return render(request, 'boards/join_board.html')
