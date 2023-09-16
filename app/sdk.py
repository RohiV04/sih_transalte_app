from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient
from decouple import config
endpoint = config('DOC_TRANSLATE_ENDPOINT')
credential = config('DOC_TRANSLATE_KEY')
source_container_sas_url_en =config('SOURCE_SASS_URL')
target_container_sas_url_es = config('TARGET_SASS_URL')

document_translation_client = DocumentTranslationClient(endpoint, credential)

poller = document_translation_client.begin_translation(source_container_sas_url_en, target_container_sas_url_es, "te")

result = poller.result()

print(f"Status: {poller.status()}")
print(f"Created on: {poller.details.created_on}")
print(f"Last updated on: {poller.details.last_updated_on}")
print(f"Total number of translations on documents: {poller.details.documents_total_count}")

print("\nOf total documents...")
print(f"{poller.details.documents_failed_count} failed")
print(f"{poller.details.documents_succeeded_count} succeeded")

for document in result:
    print(f"Document ID: {document.id}")
    print(f"Document status: {document.status}")
    if document.status == "Succeeded":
        print(f"Source document location: {document.source_document_url}")
        print(f"Translated document location: {document.translated_document_url}")
        print(f"Translated to language: {document.translated_to}\n")
    else:
        print(f"Error Code: {document.error.code}, Message: {document.error.message}\n")