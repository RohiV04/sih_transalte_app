import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from decouple import config

def recursively_remove_key(dictionary, key_to_remove):
    # Recursive function to remove a key and its associated value from a dictionary
    if isinstance(dictionary, dict):
        return {
            key: recursively_remove_key(value, key_to_remove)
            for key, value in dictionary.items()
            if key != key_to_remove
        }
    elif isinstance(dictionary, list):
        return [recursively_remove_key(item, key_to_remove) for item in dictionary]
    else:
        return dictionary

def replace_none_with_empty(dictionary):
    # Recursive function to replace None values with empty strings in a dictionary
    if isinstance(dictionary, dict):
        return {
            key: replace_none_with_empty(value)
            for key, value in dictionary.items()
            if value is not None
        }
    elif isinstance(dictionary, list):
        return [replace_none_with_empty(item) for item in dictionary]
    else:
        return dictionary

def serialize_datetime(obj):
    # Function to serialize datetime objects to string
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def extract_text_from_document(input_file_path, get_fields=False, get_tables=False, get_content=False):
    key = config('FORM_RECOGNIZER_KEY')
    endpoint = config('FORM_RECOGNIZER_ENDPOINT')
    try:
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        with open(input_file_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-document", document=f, locale="en-US"
            )

        extracted_data = poller.result()

        
        if get_fields:
            # Used for invoice extraction. Extract basic details and fields for line items.
            fields = extracted_data.to_dict()['documents']
            cleaned_fields = recursively_remove_key(fields, 'bounding_regions')
            cleaned_fields = recursively_remove_key(cleaned_fields, 'spans')
            cleaned_fields = replace_none_with_empty(cleaned_fields)
            fields_json = json.dumps(cleaned_fields, default=serialize_datetime, indent=4)
            return fields_json

        if get_tables:
            tables = extracted_data.to_dict()['tables']
            return tables

        if get_content:
            content = extracted_data.to_dict()['content']
            return content

        return extracted_data.to_dict()['content']

    except Exception as e:
        return str(e)

# Example usage:
if __name__ == "__main__":
    input_file_path = "./test/test-3.png"
    
    # Specify which data you want to retrieve by setting the corresponding flags.
    fields_data = extract_text_from_document(input_file_path, get_fields=True)
    print("Fields Data:", fields_data)
    print("-----------------------------------\n\n")
    tables_data = extract_text_from_document(input_file_path, get_tables=True)
    print("Tables Data:", tables_data)
    print("-----------------------------------\n\n")
    content_data = extract_text_from_document(input_file_path, get_content=True)
    print("Content Data:", content_data)
