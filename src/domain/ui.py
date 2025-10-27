from abc import ABC, abstractmethod


class UI(ABC):
        @abstractmethod
        def show(self) -> None:
                """Render user interface."""
