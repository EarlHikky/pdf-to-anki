# Python FAQ Anki Deck Generator

This Python script allows you to generate Anki decks from PDF files containing FAQ-style content. It extracts text from the PDF, formats it into Anki-compatible question-answer pairs, and creates an Anki deck in `.apkg` format.

## Requirements

- Python 3.x
- `genanki` library (install via `pip install genanki`)
- `pdfminer.six` library (install via `pip install pdfminer.six`)

## Usage

1. Ensure you have Python installed on your system.
2. Install required dependencies using `pip`.
3. Run the script using `python main.py <path-to-pdf> --deck_name <deck-name>`.
4 The Anki deck will be generated as `<deck-name>.apkg` in the root directory.

## Notes

- Ensure your PDF file follows a specific format where questions start with a number followed by a dot and answers are listed below each question.
- Questions and answers are separated by a newline.
- The script uses `pdfminer.six` to extract text from the PDF file, so ensure it's properly formatted and readable.
- HTML tags within questions and answers are escaped to prevent formatting issues in Anki.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

