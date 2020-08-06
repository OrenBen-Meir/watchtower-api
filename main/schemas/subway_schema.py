from typing import List


class SubwaySchema:
    def __init__(self, uuid: str, name: str, geo_position: str,
                 line: str, notes: List[str], url: str, created_at: int,
                 updated_at: int):
        self.uuid: str = uuid
        self.geo_position: str = geo_position
        self.name: str = name
        self.line: str = line
        self.notes: List[str] = notes
        self.url: str = url
        self.created_at: int = created_at
        self.updated_at: int = updated_at

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.to_dict())


class SubwayListSchema:
    def __init__(self, subways: List[SubwaySchema]):
        self.subways: List[SubwaySchema] = subways

    def to_dict(self):
        return {
            "subways": [s.to_dict() for s in self.subways]
        }

    def __str__(self):
        return str(self.to_dict())
