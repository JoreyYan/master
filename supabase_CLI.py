
import json
import os
from supabase import create_client, Client


url='https://izxsmniuqmijijowfrgo.supabase.co'
key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml6eHNtbml1cW1pamlqb3dmcmdvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzk5ODg0MSwiZXhwIjoyMDIzNTc0ODQxfQ.dCVNPGANUD8XIbyfUiooo8m4LqPepY9DszivUJtyb_Y'



import requests
import json

# openaiurl = 'https://izxsmniuqmijijowfrgo.supabase.co/functions/v1/openai'
# headers = {
#     'Content-Type': 'application/json',
#     'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml6eHNtbml1cW1pamlqb3dmcmdvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDc5OTg4NDEsImV4cCI6MjAyMzU3NDg0MX0.wYMh9ii5X2L8YbkJ1uhaU3sRjBPdZwIoBiExCJ7pq0w'
# }
# data = json.dumps({"query": "What is the capital of France?"})
#
# response = requests.post(url, headers=headers, data=data)
#
# if response.status_code == 200:
#     print("Success:", response.json())
# else:
#     print("Error:", response.status_code, response.text)






supabase: Client = create_client(url, key)
#
# resp = supabase.functions.invoke(
#   "openai",
#   invoke_options={
#
#     "body": json.dumps({
#       "query": "What is the capital of France?"
#     })
#   }
# )
# print(resp)
#
# 构造要上传的数据
data = json.dumps({
        'A': "Today is nice",
        "B": "yes"
    })


data = supabase.table('ghost_listen').insert({"id": 4, "listening": data}).execute()
print(data)
# bucket_name = "ghost_test"
#
#
# reslist = supabase.storage.list_buckets()
# print(reslist)
# with open("/home/junyu/luyin.m4a", "rb") as audio_file:
#     file_name = "news/audio.mp3"
#     response = supabase.storage.from_(bucket_name).upload(file_name, audio_file)
#     print(response)
# path_on_supastorage='your-bucket-name/audio/'
# with open("/home/junyu/luyin.m4a", 'rb') as f:
#     supabase.storage.from_(bucket_name).upload(path=path_on_supastorage,file=f, file_options={"content-type": "audio/mpeg"})