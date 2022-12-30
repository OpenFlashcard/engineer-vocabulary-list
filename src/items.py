import os
from abc import ABCMeta, abstractclassmethod
from color import Color
from model import TextFormatter
from item import Item


class PlainText(Item):
    def __init__(self, source: str):
        self.source = source
        self.format()

    def format(self, formatter: TextFormatter = None):
        self.formatted_text = self.source


class ClozeText(Item):
    def __init__(
        self,
        source: str,
        start_symbol: str,
        end_symbol: str,
        formatter: TextFormatter
    ) -> None:
        self.source = source
        self.start_symbol = start_symbol
        self.end_symbol = end_symbol
        self.format(formatter)

    def format(self, formatter: TextFormatter):
        self.formatted_text = formatter.format_cloze_text(self)


class HighlightText(Item):
    def __init__(
        self,
        source: str,
        keyword: str,
        color: Color,
        formatter: TextFormatter
    ) -> None:
        self.source = source
        self.keyword = keyword
        self.color = color
        self.format(formatter)

    # TODO Multiple Constructors
    # def __init__(
    #     self,
    #     source: str,
    #     start_symbol: str,
    #     end_symbol: str,
    #     formatter: TextFormatter
    # ) -> None:
    #     self.source = source
    #     self.start_symbol = start_symbol
    #     self.end_symbol = end_symbol
    #     self.format(formatter)

    def format(self, formatter: TextFormatter):
        self.formatted_text = formatter.format_highlight_text(self)


class File(metaclass=ABCMeta):
    def __init__(self, name: str, dir: str) -> None:
        self.name = name
        self.absolute_path = os.path.join(dir, name)

    def set_name(self, name):
        self.name = name

    def set_dir(self, dir):
        self.dir = dir

    @abstractclassmethod
    def format(self, formatter: TextFormatter):
        raise NotImplementedError


class ImageFile(Item, File):
    def __init__(self, filename: str, dir: str) -> None:
        super.__init__(filename, dir)  # File.__init__

    def format(self, formatter: TextFormatter):
        self.formatted_text = formatter.format_image_file_link(self)


class AudioFile(Item, File):
    def __init__(self, filename: str, dir: str) -> None:
        super.__init__(filename, dir)

    def format(self, formatter: TextFormatter):
        self.formatted_text = formatter.format_audio_file_link(self)
