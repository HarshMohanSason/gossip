# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore
import google.cloud.firestore
import random
import re

 app = initialize_app() #initialize the appId
 db = firestore.client()
#
#
@https_fn.on_request()

def loginUser(request):
    {
      username = request.args.get('username')
      collegeEmail = request.args.get('college_email')


    }

def validateCollegeEmail(email):
    {
         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.+-]+\.(edu)$'   #RegExp to match whether the entered email is valid or not

         return bool(re.match(pattern,email))
    }

def validateUserName(username):
    {
         pattern = r'^[a-zA-Z0-9_]+$' #username will not contain any symbols. Only alphabets and letters

         return bool(re.match(pattern,username))
    }


def checkUserExists(userName, college_email):
    {


    }
