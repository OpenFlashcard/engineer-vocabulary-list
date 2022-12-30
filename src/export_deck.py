import argparse
import os
import pandas as pd
import shutil
from models.anki import Anki
from common import Deck, Card, Color
from items import ClozeText, HighlightText, PlainText, AudioFile


INPUT_AUDIO_DIR = '../media/audio'
INPUT_IMAGE_DIR = '../media/image'
DECK_NAME = 'engineer-vocabulary-list'

parser = argparse.ArgumentParser(description='word list to flashcards.')
parser.add_argument('import_file_path', help='import csv file\'s relative path')
args = parser.parse_args()


def main() -> None:
    deck = Deck(name=DECK_NAME, cards=[])
    model = Anki()

    df = pd.read_csv(args.import_file_path)
    for _, row in df.iterrows():
        if (row['ENGLISH AUDIO FILE']):
            copy_media_file(
                DECK_NAME,
                INPUT_AUDIO_DIR,
                row['ENGLISH AUDIO FILE'],
                model.media_dir)

        card = Card(
            fields=[
                ClozeText(source=row['ENGLISH SENTENCE WITH CLOZE'],
                          start_symbol='{{',
                          end_symbol='}}',
                          formatter=model.text_formatter),
                HighlightText(source=row['JAPANESE SENTENCE'],
                              keyword=row['JAPANESE HIGHLIGHT'],
                              color=Color.BLUE,
                              formatter=model.text_formatter),
                PlainText(source=row['ENGLISH WORD']),
                PlainText(source=row['PHONETICS']),
                PlainText(source=row['JAPANESE WORD']),
                PlainText(source=row['PART OF SPEECH']),
                AudioFile(filename=concat_names(row['ENGLISH AUDIO FILE'],
                                                DECK_NAME),
                          dir=model.media_dir),
                row['SYNONYM'],
            ]
        )
        deck.cards.append(card)


def copy_media_file(deck_name: str,
                    src_dir: str,
                    filename: str,
                    dst_dir: str
                    ) -> str:
    src_path = os.path.join(src_dir, filename)
    shutil.copy(src_path, dst_dir)
    dst_path = os.path.join(dst_dir, filename)

    copied_filename = concat_names(deck_name, filename)
    renamed_dst_path = os.path.join(dst_dir, copied_filename)
    os.rename(dst_path, renamed_dst_path)


def concat_names(deck_name: str, filename: str) -> str:
    return '_'.join([deck_name, filename])


if __name__ == '__main__':
    main()
