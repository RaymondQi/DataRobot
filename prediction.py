####import the libarary:
import sys
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from apiclient.discovery import build
import json

##Create the project and train the model by Using Google Developer Console
## name depends on user

project_id = 'datarobot-960'
model_id = 'digit_learner'

#######################################Main Function################################
def main():   
      
      ####Read the credential private key from JSON FILE downloaded from GOOGLE DEVELOPER CONSOLE
      
      with open('DataRobot-ad5fdab3c6c8.json') as f1:
          #f1 is private key
          p_key = json.load(f1)
          f1.close()
      ###get the client email and private key
      
      Private_KEY = p_key['private_key']
      client_email = p_key['client_email']
      
      ###Create Signed JWT Assertion Credential
      
      scope = ['https://www.googleapis.com/auth/prediction']     
      credentials = SignedJwtAssertionCredentials(client_email, Private_KEY, scope =  scope)
     
      ###Authorization
     
      http_auth = credentials.authorize(Http())
     
      ###Access the prediction API and extracted trained model
     
      prediction = build('prediction', 'v1,6', http = http_auth)
     
      ###prediction by commandline
             
      new_sample = sys.argv[1]
      body = {"input": {"csvInstance": [new_sample] } }
      TrainedModel = prediction.trainedmodels().predict(project = project_id, id = model_id, body = body ).execute()
      print TrainedModel['outputLabel']
