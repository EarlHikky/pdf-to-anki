# Python FAQ Anki Deck Generator

This Python script allows you to generate Anki decks from PDF files containing FAQ-style content. It extracts text from the PDF, formats it into Anki-compatible question-answer pairs, and creates an Anki deck in `.apkg` format.

## Requirements

- Python 3.x
- `genanki` library (install via `pip install genanki`)
- `pdfminer.six` library (install via `pip install pdfminer.six`)

## Usage

1. Ensure you have Python installed on your system.
2. Install required dependencies using `pip`.
3. Place your PDF file containing FAQ-style content in the root directory.
4. Update the `path_to_pdf` variable in the script with the filename of your PDF.
5. Run the script using `python script_name.py`.
6. The Anki deck will be generated as `Python_FAQ.apkg` in the root directory.

## Notes

- Ensure your PDF file follows a specific format where questions start with a number followed by a dot and answers are listed below each question.
- Questions and answers are separated by a newline.
- The script uses `pdfminer.six` to extract text from the PDF file, so ensure it's properly formatted and readable.
- HTML tags within questions and answers are escaped to prevent formatting issues in Anki.

## Example

Suppose you have a PDF file named `python_faq.pdf` containing FAQ-style content. You would update the `path_to_pdf` variable in the script with `'python_faq.pdf'` and then run the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

