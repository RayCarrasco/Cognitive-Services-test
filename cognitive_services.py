# Find the subscription key and endpoint
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key =  "your-password-will-go-here"  # this have to be replaced 
endpoint =  "your-api-url-will-go-here"           # this have to be replaced

# Authentcate the client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Analyze an image, this url could be changedv  
remote_image_url = "https://www.informador.mx/__export/1586425165789/sites/elinformador/img/2020/04/09/talent_crop1586425162266.jpg_788543494.jpg"

# prcess description
print("===== Let's see the results =====")

# consume the API service with the authorize client
description_results = computervision_client.describe_image(remote_image_url)

# print the complete response
from pprint import pprint
print("=== the response structure ===")
pprint(description_results.as_dict())

print("=== show descriptions ===")

# Show responses
if len(description_results.captions) == 0:
    print("No description detected.")
else:
    for caption in description_results.captions:
        print(f"'{caption.text}' with confidence of {caption.confidence * 100:.2f}%")
