from behave import given, when, then
from pathlib import Path
from pyfakefs.fake_filesystem_unittest import Patcher


@given("The user selects a folder as {folder}")
def user_selects_folder(context, folder):
        patcher = Patcher()
        patcher.setUp()
        context.patcher = patcher
        context.fs = patcher.fs
        context.origin = folder
        context.fs.makedirs(folder, exist_ok=True)
        for f in ["F1", "F2", "F3"]:
            context.fs.create_file(Path(folder) / f)
        context.folder_files = ["F1", "F2", "F3"]


@given("{folder} is a valid path and exists")
def folder_is_a_valid_path_and_exists(context, folder):
        assert context.fs.exists(folder)


@given("{folder} is not empty")
def folder_has_files(context, folder):
        assert len(list(Path(folder).glob("**/*"))) > 0


@when("User runs program")
def user_runs_program(context):
        context.has_run = True


@then("The program processes files from the selected {folder}")
def processed_files_are_from_selected_folder(context, folder):
        context.folder = folder
        context.patcher.tearDown()
