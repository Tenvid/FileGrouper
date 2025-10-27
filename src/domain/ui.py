from abc import ABC, abstractmethod
from typing import Any


class UI(ABC):
        @abstractmethod
        def show(self) -> None:
                """Render user interface."""

        @abstractmethod
        def store_value(self, variable_name: str, value: Any) -> None:
                """Ask user to enter a value and store it in a custom variable name."""

        @abstractmethod
        def get_stored_values(self) -> dict[str, Any]:
                """Return all stored values."""
