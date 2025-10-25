from behave import given, when, then


@given("User has chosen a criteria as {criteria}")
def user_groups_by_criteria(context, criteria):
    context.group_type = criteria


@when("User groups files")
def user_groups_files(context):
    context.has_run = True


@then("Files are grouped by selected criteria as {criteria}")
def files_are_grouped_by_criteria(context, criteria):
    assert context.group_type == criteria
