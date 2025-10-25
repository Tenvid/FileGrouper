from pathlib import Path


class GroupFilesUsecase:
        def __init__(self, origin: Path, destination: Path, grouper):
                self.__origin = origin
                self.__destination = destination
                self.__grouper = grouper

        def execute(self):
                self.__grouper.group_files(self.__origin, self.__destination)
