from pathlib import Path
from src.domain.grouper import Grouper


class GroupFilesUsecase:
        def __init__(self, origin: Path, destination: Path, grouper: Grouper):
                self.__origin = origin
                self.__destination = destination
                self.__grouper = grouper

        def execute(self):
                self.__grouper.group_files(self.__origin, self.__destination)
