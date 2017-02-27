from __future__ import unicode_literals

from django.db import models
import re, bcrypt
import datetime
# Create your models here.
class UserManager(models.Manager):
    def validateAndRegisterData(self, postData):
        errors = []
        #validate first name
        if not (len(postData['firstName']) >= 2 and re.match("^[a-zA-Z]", postData['firstName'])):
            errors.append("First name not long enough")
        #validate Last name
        if not (len(postData['lastName']) >= 2 and re.match("^[a-zA-Z]", postData['lastName'])):
            errors.append("Last name not long enough")
        #validate email address
        if not re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", postData['email']):
            errors.append("Invalid email address")
        #validate password
        if  not len(postData['password']) >= 8:
            errors.append("Password must be 8 characters long")
        if not (postData['password'] == postData['passwordConf']):
            errors.append("Passwords must match")
        unique = self.filter(email=postData['email'])
        if unique:
            errors.append("Email must be unique")
        modelStatus = {}
        if errors:
            modelStatus['status'] = False
            modelStatus['errors'] = errors

        else:
            #Hash password
            hashedPW = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            #create user
            user = self.create(first_name = postData['firstName'], last_name = postData['lastName'], email = postData['email'], password=hashedPW, hired_on=postData['hireDate'])
            modelStatus['status'] = True
            modelStatus['user'] = user

        return modelStatus

    def login(self, postData):
        #check if user is in database
        user = self.filter(email=postData['loginEmail'])
        modelsResponse = {}
        #if user exists
        if user:
            #check passwords
            if bcrypt.checkpw(postData['loginPassword'].encode(), user[0].password.encode()):
                #send success to views
                modelsResponse['status'] = True
                modelsResponse['user'] = user[0]
            # fail password match
            else:
                #send error message
                modelsResponse['status'] = False
                modelsResponse['errors'] = "non-matching passwords"
        #else user not found
        else:
            #send message to views
            modelsResponse['status'] = False
            modelsResponse['errors'] = "Invalid Email"

        return modelsResponse

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    hired_on = models.DateTimeField(auto_now_add = False, default=datetime.datetime.now)
    users = UserManager()


#from django.db import connection
#
#with connection.cursor() as cursor:
#    cursor.execute("" ""
#                   "INSERT INTO User %"
#                   "", postData.firstName)

