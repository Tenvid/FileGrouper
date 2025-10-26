from abc import ABC, abstractmethod
from pathlib import Path


class Grouper(ABC):
        @abstractmethod
        def group_files(self, origin_path: Path, destination_path: Path) -> None:
                """Move files to a new folder grouped by a criteria."""
