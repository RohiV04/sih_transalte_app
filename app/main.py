from formrecogniser import extract_text_from_document
from summarize import summarize_text
from translate import translate_text

input_file_path = "../test/test-1.pdf"
target_language = "te"
extracted_text = extract_text_from_document(
    input_file_path)
if extracted_text['status']==True:
    extracted_text = extracted_text['data']
    print("Extracted text:\n", extracted_text, '\n\n')
    print("-----------------------------------\n\n")
    summarized_text = summarize_text(extracted_text)
elif extracted_text['status'] == False:
    print("Error in extracting text from document.")
    print(extracted_text['err'])
    exit()
if summarized_text['status']==True:
    summarized_text = summarized_text['data']
    print("Summarized text:\n", summarized_text, '\n\n')
    print("-----------------------------------\n\n")
    translated_text = translate_text(summarized_text, target_language)
elif summarized_text['status'] == False:
    print("Error in summarizing text.")
    print(summarized_text['err'])
    exit()
if translated_text['status']==True:
    translated_text = translated_text['data']
    print("Translated text:\n", translated_text, '\n\n')
    print("-----------------------------------\n\n")
elif translated_text['status'] == False:
    print("Error in translating text.")
    print(translated_text['err'])
    exit()

