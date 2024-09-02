# N-Gram Analyzer

N-Gram Analyzer is a Python tool for finding the most frequent sequences of N words in a PDF file, using a French word dictionary to filter out invalid words. The analysis can be customized by specifying the minimum word length to consider, the number of most frequent N-grams to display, and the size of the N-grams.

## Features

- Read and extract text from PDF files.
- Clean the text to remove special characters and normalize capitalization.
- Filter words using a French word dictionary.
- Search for sliding N-grams of a specified size.
- Display the most frequent N-grams based on defined criteria.

## Prerequisites

Before running the script, ensure you have installed the necessary Python libraries:

- PyPDF2

You can install this library using pip:

```bash
# Install PyPDF2 using pip.
pip install PyPDF2
```
# Installation

    Clone this repository to your local machine.

```bash
# Clone the repository.
git clone https://github.com/your-username/NGramAnalyzer.git
#  Navigate to the project directory.
cd NGramAnalyzer
# Install the required Python dependencies.
pip install -r requirements.txt
```
# Usage

The main script is main.py. You can run the script from the command line with the appropriate arguments.
Command Syntax

```bash
python main.py <path_to_pdf> <path_to_dictionary> [-n <ngram_size>] [-t <top_ngrams>] [-m <min_word_length>]
```
# Arguments

    <path_to_pdf>: Path to the PDF file to be analyzed.
    <path_to_dictionary>: Path to the text file containing the list of French words.
    -n, --ngrams: (optional) Length of the sliding N-grams. Default value: 3.
    -t, --top: (optional) Number of most frequent N-grams to display. Default value: 1.
    -m, --min_length: (optional) Minimum length of words to consider. Default value: 3.

# Example Command

Here is an example command to analyze a PDF file with 4-word N-grams, displaying the top 10 most frequent, and considering only words with 3 or more letters:

```bash
python main.py '..\..\Downloads\03.pdf' '..\..\Downloads\liste.de.mots.francais.frgut.txt' -m 3 -t 10 -n 4
```
# Output

The script will display the most frequent N-grams and the number of times they appear, based on the specified criteria.
Logging

The script uses the logging library to provide information about execution steps such as reading the PDF file, cleaning the text, loading the dictionary, and searching for N-grams. The log messages help to understand the processing flow and diagnose potential issues.