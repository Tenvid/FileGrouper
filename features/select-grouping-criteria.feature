Feature: Group files by criteria

  Scenario Outline: User groups files by a given criteria as '<criteria>'
    Given User has chosen a criteria as '<criteria>'
    When User groups files
    Then Files are grouped by selected criteria as '<criteria>'

    Examples:
      | criteria     |
      | Type         |
      | Size         |
      | Name Pattern |

  Scenario: User groups files by size
    Given User leaves default size grouping settings
    When User groups files by Size
    Then Files are grouped by size

  Scenario: User groups files by type
    When User groups files by Type
    Then Files are grouped by type
