from behave import given, when, then
from pyfakefs.fake_filesystem_unittest import Patcher

# User groups files by a given criteria as '<criteria>'

@given("User has chosen a criteria as {criteria}")
def user_groups_by_criteria(context, criteria):
        context.group_type = criteria


@when("User groups files")
def user_groups_files(context):
        context.has_run = True


@then("Files are grouped by selected criteria as {criteria}")
def files_are_grouped_by_criteria(context, criteria):
        assert context.group_type == criteria


# User groups files by size

@given("User leaves default size grouping settings")
def user_leaves_default_size_grouping_settings(context):
        context.patcher = Patcher()
        context.patcher.setUp()
        context.fs = context.patcher.fs
        context.fs.makedir("origin_folder")
        context.fs.makedir("destination_folder")
        context.slices = [1, 10, 100, 500, 1024]
        context.origin = "origin_folder"
        context.destination = "destination_folder"

@when("User groups files by Size")
def user_groups_files_by_size(context):
        for slice in context.slices:
            context.fs.makedir(f"{context.origin}/{slice}")

@then("Files are grouped by size")
def files_are_grouped_by_size_ranges(context):
        for slice in context.slices:
            assert context.fs.exists(f"{context.origin}/{slice}")
        context.patcher.tearDown()
