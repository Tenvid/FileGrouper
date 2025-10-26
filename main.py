from pathlib import Path
from src.application.GroupFilesUsecase import GroupFilesUsecase
from src.domain.size_grouper import SizeGrouper


def main() -> None:
        raw_origin_path = input("Enter the origin folder path: ")
        raw_destination_path = input("Enter the destination folder path: ")
        grouper = SizeGrouper()
        usecase = GroupFilesUsecase(
                origin=Path(raw_origin_path),
                destination=Path(raw_destination_path),
                grouper=grouper,  # TODO: Select Grouper implementation
        )
        usecase.execute()


if __name__ == "__main__":
        main()
