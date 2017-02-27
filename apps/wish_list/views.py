from django.shortcuts import render, HttpResponse, redirect
from models import Item
from ..loginAndReg.models import User
# Create your views here.
def landing(request):
    context = {
        'thisUser' : User.users.get(id=request.session['userID']),
    }
    # Find all items attached to this user
    context['allItems'] = Item.objects.filter(added_by=context['thisUser'])
    # Find all itmes attached to this user, excluding those not created this user
    context['othersItems'] = Item.objects.all().exclude(added_by=context['thisUser']).exclude(wanted_by=context['thisUser'])
    # Find all items attached to this user, excluding those created by this user
    context['wantedItems'] = Item.objects.filter(wanted_by=context['thisUser']).exclude(added_by=context['thisUser'])
    return render(request, 'wish_list/landing.html', context)


def productInfo(request, target):
    context = {}
    # Find current item
    context['thisItem'] = Item.objects.get(id = target)
    # Generate wanters list
    context['allWhoWant'] = context['thisItem'].wanted_by.all
    return render(request, 'wish_list/moreInfo.html', context)

def addItem(request):
    return render(request, 'wish_list/addItem.html')

def addProduct(request):
    context = {}
    # Get user object from user ID
    context['thisUser'] = User.users.get(id = request.session['userID'])
    # Create new item
    item = Item.objects.create(item_name = request.POST['itemName'], added_by = context['thisUser'])
    # Attach item to user
    item.wanted_by.add(context['thisUser'])

    return landing(request)

def delete(request, target):
    # Delete selected item
    Item.objects.get(id = target).delete()
    return landing(request)

def addToCurrentUser(request, target):
    # Collect currentUser and the target item objects
    targetItem = Item.objects.get(id = target)
    currentUser = User.users.get(id = request.session['userID'])
    # Append target item to current user's want list
    currentUser.wanted_by.add(targetItem)
    # Append user to target items wanters list
    targetItem.wanted_by.add(currentUser)
    return landing(request)

def removeFromCurrentUser(request, target):
    # Find item
    targetItem = Item.objects.get(id = target)
    # Find user
    currentUser = User.users.get(id = request.session['userID'])
    # Remove item from user's wanted list
    currentUser.wanted_by.remove(targetItem)
    return landing(request)