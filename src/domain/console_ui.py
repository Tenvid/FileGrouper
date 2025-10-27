from src.domain.ui import UI


class ConsoleUI(UI):
        def show(self) -> None:
                print("Introduce el tipo de agrupamiento que deseas aplicar: ")
                print("1 - Tamaño")
                print("2 - Tipo")
                print("3 - Patrón")
