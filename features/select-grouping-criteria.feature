Feature: Agrupar los ficheros

  Scenario Outline: User groups files by a given criteria as '<criteria>'
    Given User has chosen a criteria as '<criteria>'
    When User groups files
    Then Files are grouped by selected criteria as '<criteria>'

    Examples:
      | criteria         |
      | Tipo             |
      | Tamaño           |
      | Patrón de nombre |
