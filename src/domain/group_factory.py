from src.domain.group_type import GroupType
from src.domain.grouper import Grouper
from src.domain.size_grouper import SizeGrouper


class GroupFactory:
        def build(self, group_type: GroupType) -> Grouper:
                if group_type == GroupType.SIZE:
                        return SizeGrouper()
                if group_type == GroupType.PATTERN:
                        raise NotImplementedError
                if group_type == GroupType.TYPE:
                        raise NotImplementedError
                else:
                        raise TypeError("Unexpected group type")
