import PyPDF2
from collections import Counter
import re
import argparse
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_pdf(pdf_file_path):
    """
    Reads the PDF file and extracts the text.
    """
    logging.info(f"Reading the PDF file: {pdf_file_path}")
    text = ""
    try:
        with open(pdf_file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        logging.info(f"Text extraction from PDF file completed. Length of extracted text: {len(text)} characters.")
    except Exception as e:
        logging.error(f"Error reading the PDF file: {e}")
    return text

def clean_text(text):
    """
    Cleans the text by removing special characters, digits, and converting everything to lowercase.
    """
    logging.info("Cleaning the text...")
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = text.lower()
    logging.info(f"Text cleaning completed. Length of cleaned text: {len(text)} characters.")
    return text

def load_dictionary(dictionary_path):
    """
    Loads the French dictionary from a file and cleans each word.
    """
    logging.info(f"Loading dictionary from: {dictionary_path}")
    try:
        with open(dictionary_path, 'r', encoding='utf-8') as file:
            french_words = set(clean_text(file.read()).split())
        logging.info(f"Dictionary loaded successfully. Number of words in dictionary: {len(french_words)}")
    except Exception as e:
        logging.error(f"Error loading the dictionary: {e}")
        french_words = set()
    return french_words

def filter_words(text, french_words, min_length):
    """
    Filters the words in the text to keep only those that are in the French dictionary and have at least 'min_length' characters.
    """
    logging.info(f"Filtering text words to keep only valid French words with at least {min_length} characters.")
    words = text.split()
    filtered_words = [word for word in words if word in french_words and len(word) >= min_length]
    logging.info(f"Filtering completed. Number of words after filtering: {len(filtered_words)}")
    return ' '.join(filtered_words)

def find_sliding_ngrams(text, n):
    """
    Finds sliding N-grams in the filtered text.
    """
    logging.info(f"Searching for sliding N-grams of length {n}.")
    words = text.split()
    ngram_count = Counter()

    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i+n])
        ngram_count[ngram] += 1

    logging.info(f"N-gram search completed. Total number of N-grams found: {len(ngram_count)}")
    return ngram_count

def main():
    parser = argparse.ArgumentParser(description="Find the most frequent sequences of N words in a PDF.")
    parser.add_argument("pdf_file", type=str, help="Path to the PDF file to be analyzed.")
    parser.add_argument("dictionary", type=str, help="Path to the French dictionary file.")
    parser.add_argument("-n", "--ngrams", type=int, default=3, help="Length of sliding N-grams (default: 3).")
    parser.add_argument("-t", "--top", type=int, default=1, help="Number of most frequent N-grams to display (default: 1).")
    parser.add_argument("-m", "--min_length", type=int, default=3, help="Minimum length of words to consider (default: 3).")

    args = parser.parse_args()

    logging.info("Starting analysis.")
    text = read_pdf(args.pdf_file)
    cleaned_text = clean_text(text)
    french_words = load_dictionary(args.dictionary)
    filtered_text = filter_words(cleaned_text, french_words, args.min_length)
    ngram_count = find_sliding_ngrams(filtered_text, args.ngrams)
    most_common_ngrams = ngram_count.most_common(args.top)

    logging.info(f"Displaying the top {args.top} most frequent N-grams.")
    for ngram, frequency in most_common_ngrams:
        formatted_ngram = ' '.join(ngram)
        print(f"'{formatted_ngram}' appears {frequency} times.")
    logging.info("Analysis completed.")

if __name__ == "__main__":
    main()