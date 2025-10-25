Feature: Select origin of files

  Scenario Outline: User selects the origin folder of the files
    Given The user selects a folder as '<folder>'
    And '<folder>' is a valid path and exists
    And '<folder>' is not empty
    When User runs program
    Then The program processes files from the selected '<folder>'

    Examples:
      | folder                        |
      | C:\\Users\\JohnDoe\\Documents |
      | /home/JaneDoe/Documents       |
