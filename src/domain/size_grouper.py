from src.domain.grouper import Grouper
from pathlib import Path


class SizeGrouper(Grouper):
        def group_files(self, origin_path: Path, destination_path: Path) -> None:
                slices = [
                        (0.0, 1.0),
                        (1.0, 10.0),
                        (10.0, 100.0),
                        (100.0, 500.0),
                        (500.0, 1024.0),
                        (1024.0, 10.0 * 1024.0),
                        (10.0 * 1024.0, float("inf")),
                ]  # TODO: Sizes should be entered by user

                for slice in slices:
                        slice_folder = destination_path / f"{slice[0]}-{slice[1]}KB"
                        slice_folder.mkdir(parents=True, exist_ok=True)

                for file in origin_path.iterdir():
                        if not file.is_file():
                                continue
                        file_size_kb = self.__get_file_size(file)
                        for slice in slices:
                                if self.__is_file_size_out_of_range(slice, file_size_kb):
                                        continue
                                target_path = self.__build_target_path(destination_path, slice, file)
                                file.rename(target_path)
                                break

        def __is_file_size_out_of_range(self, slice: tuple[float, float], file_size_kb: float) -> bool:
                return file_size_kb < slice[0] or file_size_kb > slice[1]

        def __get_file_size(self, file: Path) -> float:
                return file.stat().st_size / 1024

        def __build_target_path(self, destination_path: Path, slice: tuple[float, float], file: Path) -> Path:
                target_folder = self.__build_target_folder(
                        destination_path,
                        slice,
                )
                target_path = target_folder / file.name
                return target_path

        def __build_target_folder(self, destination_path: Path, slice: tuple[float, float]) -> Path:
                return destination_path / f"{slice[0]}-{slice[1]}KB"
