
# coding: utf-8

# In[13]:

import pprint
import boto3
import os
import requests
import json
import cv2
# Set the  percentage of 'similarity'
# our choice
SIMILARITY_THRESHOLD = 80.0

# In[17]:
    
# Read credentials from the environment
key        = os.environ.get('AWS_ACCESS_KEY_ID')
secret     = os.environ.get('AWS_SECRET_ACCESS_KEY')
region     = 'us-east-1'
Directory  = 'E:\Balaji\Visa docs\Target'
    #print(key)
    #print(secret)
    #print(region)
    
client = boto3.client('rekognition',aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)

# Our source image:
with open('E:\Balaji\Visa docs\Source\driver.jpg', 'rb') as source_image:
    source_bytes = source_image.read()

# Our target image:
    
#with open('E:\Balaji\Visa docs\Target\Target.jpg','rb') as target_image:
#    target_bytes = target_image.read()
        
    for filename in os.listdir(Directory):
        print(filename)
        print(os.path.join(Directory, filename))
        with open(os.path.join(Directory, filename),'rb') as target_image:
            target_bytes = target_image.read()        
        
        cresponse = client.compare_faces(
                   SourceImage={ 'Bytes': source_bytes },
                   TargetImage={ 'Bytes': target_bytes },
                   SimilarityThreshold=SIMILARITY_THRESHOLD                   
                    )    
          
        if len(cresponse['FaceMatches']) == 0:
                dauth_msg ='Unidentified Driver in the vehicle'
                print('Unidentified Driver in the vehicle')
        else:
                print(cresponse['FaceMatches'][0]['Similarity'])
                print('Driver Authentication successful') 
                print(filename.split('.')[0])                
                dname=filename.split('.')[0]
                dauth='Driver Authentication successful :' 
                mauth_flag=1
                dauth_conf=str(cresponse['FaceMatches'][0]['Similarity'])
                dauth_msg = dauth + dname
                break      

if mauth_flag == 1:

   dresponse = client.detect_faces(
   Image={ 'Bytes': target_bytes },
   Attributes=['ALL',])                                  
   
if len(dresponse['FaceDetails']) != 0:       
    emotion=dresponse['FaceDetails'][0]['Emotions']
    eyesopen=dresponse['FaceDetails'][0]['EyesOpen'] 
    mauth_flag=0
else:
    dface_msg='No response from AWS Face detection'


#print(emotion)
eyes_msg = 'Driver eyes open : ' + str(eyesopen['Value'])
print(eyes_msg)

key,value = max(item.items() for item in emotion)
mood_msg = "Driver mood detect : " + str(key) + str(value)
#print(mood_msg)

#Full message details
dface_msg = eyes_msg + '  ' + '  '+ mood_msg
print(dface_msg)      

 
# In[19]:

from twilio.rest import TwilioRestClient

account_sid = "################" # Your Account SID from www.twilio.com/console
auth_token  = "################"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message1 = client.messages.create(body=dauth_msg,
    to="+919629560098",    # Replace with your phone number
    from_="+18134403148") # Replace with your Twilio number

message2 = client.messages.create(body=dface_msg,
    to="+919944772296",    # Replace with your phone number
    from_="+18134403148") # Replace with your Twilio number

print(message1.sid)
print(message2.sid)

