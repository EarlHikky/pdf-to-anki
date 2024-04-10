import html

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


def make_anki_deck():
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
        deck_id = hash("Python_FAQ_Deck")
        deck = genanki.Deck(deck_id, "Python FAQ Deck")

        # Generate a unique identifier for the model
        model_id = hash("Python_FAQ_Model")
        model = genanki.Model(model_id, "Python FAQ Model",
                              fields=[{"name": "Question"}, {"name": "Answer"}],
                              templates=[{"name": "Card 1", "qfmt": "{{Question}}",
                                          "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}"}])

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
        package.write_to_file("Python_FAQ.apkg")


def main():
    save_pdf_to_txt('1.pdf')
    make_anki_deck()


if __name__ == '__main__':
    main()
