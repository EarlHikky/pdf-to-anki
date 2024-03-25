import html

import genanki

from pdfminer.high_level import extract_text


def save_pdf_to_txt(path_to_pdf):
    pdf_text = extract_text(path_to_pdf)
    with open('tmp.txt', 'w') as f:
        f.write(pdf_text)


def make_anki_deck():
    with open('tmp.txt', 'r') as file:
        first_question = ''
        question = ''
        answer = ''

        deck_id = hash("Python_FAQ_Deck")
        deck = genanki.Deck(deck_id, "Python FAQ Deck")

        # Создаем Anki Model
        model_id = hash("Python_FAQ_Model")
        model = genanki.Model(model_id, "Python FAQ Model",
                              fields=[{"name": "Question"}, {"name": "Answer"}],
                              templates=[{"name": "Card 1", "qfmt": "{{Question}}",
                                          "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}"}])

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
                        answer += line
                else:
                    answer += line
        package = genanki.Package(deck)
        package.write_to_file("Python_FAQ.apkg")


def main():
    save_pdf_to_txt('1.pdf')
    make_anki_deck()


if __name__ == '__main__':
    main()
