import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from items import ClozeText, HighlightText, ImageFile, AudioFile
from common import TextFormatter, Model, Deck


class _AnkiTextFormatter(TextFormatter):
    def format_cloze_text(self, text: ClozeText) -> str:
        formatted_text = text.source \
            .replace(text.start_symbol, '{{c1::') \
            .replace(text.end_symbol, '}}')
        return formatted_text

    def format_highlight_text(self, text: HighlightText) -> str:
        formatted_text = text.source \
            .replace(text.keyword,
                     '<font color="' + text.color + '">'
                     + text.keyword + '</font>')
        return formatted_text

    def format_image_fileLink(self, file: ImageFile) -> str:
        formatted_text = '<img src=' + file.name + '/>'
        return formatted_text

    def format_audio_fileLink(self, file: AudioFile) -> str:
        formatted_text = '[sound:' + file.name + ']'
        return formatted_text


class Anki(Model):
    text_formatter = _AnkiTextFormatter()
    export_dir = 'anki'
    media_dir = os.path.join(export_dir, 'media')

    def export(self, deck: Deck):
        csv_filename = deck.id + '.csv'
        with open(os.path.join(self.export_dir, csv_filename), 'w') as f:
            writer = csv.writer(f, delimiter=self.filed_separator)
            for card in deck.cards:
                writer.writerow(list(map(lambda f: f.value, card.fields)))
