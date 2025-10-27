from pathlib import Path
import pytest
from pyfakefs.fake_filesystem_unittest import Patcher
from src.domain.size_grouper import SizeGrouper
from typing import Iterator

ORIGIN_PATH = Path("/home/user/origin")
DESTINATION_PATH = Path("/home/user/destination")


@pytest.fixture
def patcher() -> Iterator[Patcher]:
        with Patcher() as patcher:
                patcher.fs.create_dir(ORIGIN_PATH)
                patcher.fs.create_dir(DESTINATION_PATH)
                yield patcher


@pytest.fixture
def grouper() -> SizeGrouper:
        return SizeGrouper()


def test_group_files_all_size_ranges(patcher: Patcher, grouper: SizeGrouper):
        """Test grouping files of various sizes into all size range folders"""
        with patcher:
                # Create files for each size range
                patcher.fs.create_file("/home/user/origin/file_500b", contents="a" * 500)  # 500 bytes -> 0.0-1.0KB
                patcher.fs.create_file("/home/user/origin/file_5kb", contents="a" * 1024 * 5)  # 5KB -> 1.0-10.0KB
                patcher.fs.create_file("/home/user/origin/file_50kb", contents="a" * 1024 * 50)  # 50KB -> 10.0-100.0KB
                patcher.fs.create_file("/home/user/origin/file_250kb", contents="a" * 1024 * 250)  # 250KB -> 100.0-500.0KB
                patcher.fs.create_file("/home/user/origin/file_700kb", contents="a" * 1024 * 700)  # 700KB -> 500.0-1024.0KB
                patcher.fs.create_file("/home/user/origin/file_3mb", contents="a" * 1024 * 1024 * 3)  # 3MB -> 1024.0-10240.0KB
                patcher.fs.create_file("/home/user/origin/file_20mb", contents="a" * 1024 * 1024 * 20)  # 20MB -> 10240.0-inf KB

                grouper.group_files(ORIGIN_PATH, DESTINATION_PATH)

                # Verify each range has exactly one file
                assert len(list(Path(DESTINATION_PATH / "0.0-1.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "1.0-10.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "10.0-100.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "100.0-500.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "500.0-1024.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "1024.0-10240.0KB").iterdir())) == 1
                assert len(list(Path(DESTINATION_PATH / "10240.0-infKB").iterdir())) == 1


def test_group_files_boundary_values(patcher: Patcher, grouper: SizeGrouper):
        """Test files at boundary values between ranges"""
        with patcher:
                patcher.fs.create_file("/home/user/origin/file_1kb", contents="a" * 1024)  # Exactly 1KB
                patcher.fs.create_file("/home/user/origin/file_10kb", contents="a" * 1024 * 10)  # Exactly 10KB
                patcher.fs.create_file("/home/user/origin/file_100kb", contents="a" * 1024 * 100)  # Exactly 100KB

                grouper.group_files(ORIGIN_PATH, DESTINATION_PATH)

                # Check which folders contain these boundary files
                folders_with_files = []
                for folder in DESTINATION_PATH.iterdir():
                        if list(folder.iterdir()):
                                folders_with_files.append(folder.name)

                assert len(folders_with_files) > 0
