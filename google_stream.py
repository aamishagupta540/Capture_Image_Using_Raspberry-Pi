from PIL import Image
import io
import requests
api_key="your_key"
from apiclient.discovery import build
import azure
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

block_blob_service =BlockBlobService(account_name="your_account_name",account_key="account_key")

resource=build("customsearch","v1",developerKey=api_key).cse()
images=[]


for i in range(1,50,10):
    result=resource.list(q="your_query",cx="cx_of_your_site",searchType="image",start=i).execute()
    images+=result["items"]

for item in images:
    response=requests.get(item["link"])  
    block_blob_service.create_blob_from_stream('account_name','external',io.BytesIO(response.content),content_settings=ContentSettings(content_type='image/Jpeg'))
    
    
