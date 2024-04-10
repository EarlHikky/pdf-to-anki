import argparse
import html
import os

import genanki

from pdfminer.high_level import extract_text


def save_pdf_to_txt(path_to_pdf):
    """
    Extracts text from a PDF file and saves it to a text file.

    Args:
        path_to_pdf (str): The path to the PDF file to extract text from.
    """
    pdf_text = extract_text(path_to_pdf)
    with open('tmp.txt', 'w') as f:
        f.write(pdf_text)


def make_anki_deck(deck_name):
    """
    Create an Anki deck from the contents of a file 'tmp.txt',
    and write the deck to a file 'Python_FAQ.apkg'.
    """
    # Open the file
    with open('tmp.txt', 'r') as file:
        first_question = ''
        question = ''
        answer = ''

        # Generate a unique identifier for the deck
        deck_id = hash(deck_name)
        deck = genanki.Deck(deck_id, deck_name)

        # Generate a unique identifier for the model
        model_id = hash(deck_name)
        model = genanki.Model(model_id, deck_name,
                              fields=[{'name': 'Question'}, {'name': 'Answer'}],
                              templates=[{'name': 'Card 1', 'qfmt': '{{Question}}',
                                          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'}])

        # Iterate through the file
        for index, raw_line in enumerate(file):
            line = raw_line.strip()

            if line:
                first_word = line.split()[0]
                if first_word.endswith('.'):
                    try:
                        float(first_word)

                        if first_word.startswith('1.'):
                            first_question = line
                            continue
                        if first_word.startswith('2.'):
                            note = genanki.Note(model=model, fields=[html.escape(first_question), html.escape(answer)])
                        else:
                            note = genanki.Note(model=model, fields=[question, html.escape(answer)])
                        deck.add_note(note)
                        question = html.escape(line)
                        answer = ''

                    except ValueError as e:
                        answer += ' ' + line
                else:
                    answer += ' ' + line
        # Create and save the deck to a file
        package = genanki.Package(deck)
        package.write_to_file(f'{deck_name}.apkg')
        os.remove('tmp.txt')


def main():
    parser = argparse.ArgumentParser(description='Convert PDF to text and generate Anki deck.')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--deck_name', type=str, help='Name of the Anki deck (default: PDF filename)', default=None)
    args = parser.parse_args()

    save_pdf_to_txt(args.pdf_path)
    deck_name = args.deck_name if args.deck_name else os.path.splitext(os.path.basename(args.pdf_path))[0]
    make_anki_deck(deck_name)


if __name__ == '__main__':
    main()
