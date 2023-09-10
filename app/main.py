from formrecogniser import extract_text_from_document
from summarize import summarize_text
from translate import translate_text

input_file_path = "../Sih Solution.pdf"
target_language = "te"
extracted_text = extract_text_from_document(
    input_file_path)
print("Extracted text:\n", extracted_text,'\n\n')
print("-----------------------------------\n\n")
summarized_text = summarize_text(extracted_text)
print("Summarized text:\n", summarized_text,'\n\n')
print("-----------------------------------\n\n")
translated_text = translate_text(summarized_text, target_language)
print("Translated text:\n", translated_text,'\n\n')
