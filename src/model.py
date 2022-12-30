import re
from abc import ABCMeta, abstractclassmethod, abstractproperty
from items import ClozeText, HighlightText, ImageFile, AudioFile


class TextFormatter(metaclass=ABCMeta):
    def format_cloze_text(self, text: ClozeText) -> str:
        formatted_text = re.sub(
            r"{}*{}".format(text.start_symbol, text.end_symbol),
            "_",
            text.source
        )
        return formatted_text

    @abstractclassmethod
    def format_highlight_text(self, text: HighlightText) -> str:
        raise NotImplementedError

    @abstractclassmethod
    def format_image_file_link(self, file: ImageFile) -> str:
        raise NotImplementedError

    @abstractclassmethod
    def format_audio_file_link(self, file: AudioFile) -> str:
        raise NotImplementedError


class Model(ABCMeta):
    field_separator = '\t'

    @abstractproperty
    def text_formatter(self):
        raise NotImplementedError

    @abstractproperty
    def export_dir(self):
        raise NotImplementedError

    def format_item_text(self, deck: Deck):
        for card in deck.cards:
            for field in card:
                for item in field:
                    item.format(self.text_formatter)

    def export_fields(fields: List[Field]):
        pass

    def export_deck(deck: Deck):
        pass
