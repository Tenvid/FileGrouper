from src.domain.grouper import Grouper
from pathlib import Path


class SizeGrouper(Grouper):
        def group_files(self, origin_path: Path, destination_path: Path) -> None:
                slices = [
                        (0, 1),
                        (1, 10),
                        (10, 100),
                        (100, 500),
                        (500, 1024),
                        (1024, 10 * 1024),
                        (10 * 1024, float("inf")),
                ]  # TODO: Sizes should be entered by user

                for slice in slices:
                        slice_folder = destination_path / f"{slice[0]}-{slice[1]}KB"
                        slice_folder.mkdir(parents=True, exist_ok=True)

                for file in origin_path.iterdir():
                        if file.is_file():
                                file_size_kb = file.stat().st_size / 1024
                                for slice in slices:
                                        if slice[0] < file_size_kb <= slice[1]:
                                                target_folder = (
                                                        destination_path
                                                        / f"{slice[0]}-{slice[1]}KB"
                                                )
                                                target_path = target_folder / file.name
                                                file.rename(target_path)
                                                break
