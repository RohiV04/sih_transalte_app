import requests
endpoint = 'https://csg-sih.cognitiveservices.azure.com/'
key =  '9003c0bcac2847de868b89bb27d2f988'
path = 'translator/text/batch/v1.1/batches'
constructed_url = endpoint + path

sourceSASUrl = 'https://csg1003200288dd9cc6.blob.core.windows.net/inputdocs?sp=r&st=2023-09-15T08:39:29Z&se=2023-09-15T16:39:29Z&spr=https&sv=2022-11-02&sr=c&sig=3PJIh50Gh9a7f3zeeZdo7oQJE3c4MUm5ObgkOaobgx8%3D'

targetSASUrl = 'https://csg1003200288dd9cc6.blob.core.windows.net/translateddocs?sp=r&st=2023-09-15T08:40:28Z&se=2023-09-15T16:40:28Z&spr=https&sv=2022-11-02&sr=c&sig=xOP9t4a7m8gEWXZhZdmfppE5fxcZKW3HYJsDJW%2FlziU%3D'

body= {
    "inputs": [
        {
            "source": {
                "sourceUrl": sourceSASUrl,
                "storageSource": "AzureBlob",
                "language": "en"
            },
            "targets": [
                {
                    "targetUrl": targetSASUrl,
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": "hi"
                }
            ]
        }
    ]
}
headers = {
  'Ocp-Apim-Subscription-Key': key,
  'Content-Type': 'application/json',
}

response = requests.post(constructed_url, headers=headers, json=body)
response_headers = response.headers

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\n\nresponse headers:\n')

for key, value in response_headers.items():
    print(key, ":", value)