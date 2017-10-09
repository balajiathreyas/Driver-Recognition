# Driver-Recognition
Filewatcher.py :
This code calls the code driver authorization with execution delay (sleep option) for demo purpose.
The code can be automated using watchdog package in python for different usage and triggers.

DriverAuth.py
  This code invokes the AWS Rekognition by sending image bytes and getting the Json reply back from Rekognition.
  One has to connect to the AWS system by giving password and secret key first to use this service.
  Two calls has been made to Rekonition :
    1. Call for driver authentication by face comparison and check the confidence. We have the source image coming from camera or any image capturing source to be compared against the authorized personnel list from the database. If the image matches the authorized personnel list then we authorize the person by sending in the message via email or mobile.
    2. Call for Driver mood detection :
       For any authorized driver or personnel we can check his mood and drowsiness state by this call to AWS Rekognition.
    
