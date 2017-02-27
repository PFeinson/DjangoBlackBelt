from django.shortcuts import render, HttpResponse, redirect
from ..loginAndReg.models import User
from ..wish_list.views import landing
# Create your views here.
def index(request):
    return render(request, 'loginAndReg/index.html')

def validate(request):
    # Attempt to validate and register
    responseFromModels = User.users.validateAndRegisterData(request.POST)
    #Success state
    if responseFromModels['status']:
        request.session['user'] = responseFromModels['user'].first_name
        return index(request)
    # Fail state
    else:
        for error in responseFromModels['errors']:
            print error
        return index(request)

def login(request):
    responseFromModels = User.users.login(request.POST)
    # if valid user, set active user credentials
    if responseFromModels['status']:
        request.session['userFirstName'] = responseFromModels['user'].first_name
        request.session['userLastName'] = responseFromModels['user'].last_name
        request.session['userID'] = responseFromModels['user'].id
        return success(request)
    else:
        # else return errors
        print responseFromModels['errors']
        context = {'errors':responseFromModels['errors']}
        return render(request, 'loginAndReg/index.html', context)

def success(request):
    if not 'user' in request.session:
        index(request)
    return landing(request)
    #return render(request, 'loginAndReg/success.html', request.session)

