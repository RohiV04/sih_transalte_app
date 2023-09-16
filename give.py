import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from decouple import config

def extract_text_from_document(input_file_path, endpoint, key):
    try:
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        with open(input_file_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-document", document=f, locale="en-US"
            )

        extracted_data = poller.result()

        if extracted_data:
            return extracted_data.to_dict()['content']
        else:
            return "No content extracted from the document."

    except Exception as e:
        return str(e)

def summarize_text(input_text):
    try:
        url = "https://open-ai21.p.rapidapi.com/summary"
        payload = {"text": input_text}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": config('OPENAI_SUMMARIZE_API_KEY'),
            "X-RapidAPI-Host": "open-ai21.p.rapidapi.com",
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()['result']
        else:
            return "Summarization failed."

    except Exception as e:
        return str(e)

def translate_text(input_text, target_language):
    try:
        translation_url = "https://text-translator2.p.rapidapi.com/translate"
        translation_payload = {
            "text": input_text,
            "source_language": "en",
            "target_language": target_language,
        }
        translation_headers = {
            "content-type": 'application/x-www-form-urlencoded',
            "Accept-Encoding": 'application/gzip',
            "X-RapidAPI-Key": config('TRANSLATE_API_KEY'),
            "X-RapidAPI-Host": 'text-translator2.p.rapidapi.com',
        }

        translation_response = requests.post(
            translation_url, data=translation_payload, headers=translation_headers)

        if translation_response.status_code == 200:
            return translation_response.json()['data']['translatedText']
        else:
            return "Translation failed."

    except Exception as e:
        return str(e)

# Example usage:
if __name__ == "__main__":
    endpoint = "https://rohi-123.cognitiveservices.azure.com/"
    form_recognizer_key = config('FORM_RECOGNIZER_KEY')
    input_file_path = "./Sih Solution.pdf"
    target_language = "te"

    extracted_text = extract_text_from_document(
        input_file_path, endpoint, form_recognizer_key)
    print("Extracted text:", extracted_text)

    summarized_text = summarize_text(extracted_text)
    print("Summarized text:", summarized_text)

    translated_text = translate_text(summarized_text, target_language)
    print("Translated text:", translated_text)
