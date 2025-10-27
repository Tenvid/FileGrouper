from typing import Any
from src.domain.ui import UI


class ConsoleUI(UI):
        def __init__(self) -> None:
                self.__attribute_names: list[str] = []

        def show(self) -> None:
                while True:
                        print("Introduce el tipo de agrupamiento que deseas aplicar: ")
                        print("1 - Tamaño")
                        print("2 - Tipo")
                        print("3 - Patrón")
                        try:
                                self.store_value("grouper_type", int(input()))
                                if 1 <= getattr(self, "grouper_type") <= 3:
                                        return

                        except ValueError:
                                continue

        def store_value(self, variable_name: str, value: Any) -> None:
                setattr(self, variable_name, value)
                self.__attribute_names.append(variable_name)

        def get_stored_values(self) -> dict[str, Any]:
                result = {}
                for name in self.__attribute_names:
                        result[name] = getattr(self, name)
                return result
