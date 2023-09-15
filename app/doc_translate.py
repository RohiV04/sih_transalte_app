import requests
from decouple import config
endpoint = config('DOC_TRANSLATE_ENDPOINT')
key =  config('DOC_TRANSLATE_KEY')
path = 'translator/text/batch/v1.1/batches'
constructed_url = endpoint + path

sourceSASUrl = config('SOURCE_SAS_URL')

targetSASUrl = config('TARGET_SAS_URL')

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