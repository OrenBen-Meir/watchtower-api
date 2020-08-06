from typing import List

import re
import requests
from main.schemas.subway_schema import SubwaySchema, SubwayListSchema


def _parse_geo_location(position: str):
    location: List[str] = re.findall(r"[-+]?\d*\.\d+|\d+", position)
    location.reverse()
    return ", ".join(location)


def get_subways() -> SubwayListSchema:
    request_ref = "https://data.cityofnewyork.us/api/views/kk4q-3rt2/rows.json"
    headers = {"content-type": "application/json; charset=UTF-8"}
    request_object = requests.get(request_ref, headers=headers)
    json = request_object.json()

    columns_list = [column_info["name"] for column_info in json["meta"]["view"]["columns"]]
    columns_to_position = {}
    for i in range(len(columns_list)):
        columns_to_position[columns_list[i]] = i

    subways: List[SubwaySchema] = []
    for data_row in json["data"]:
        subways.append(SubwaySchema(
            uuid=data_row[columns_to_position['id']],
            name=data_row[columns_to_position['NAME']],
            geo_position=_parse_geo_location(data_row[columns_to_position['the_geom']]),
            line=data_row[columns_to_position['LINE']],
            notes=data_row[columns_to_position['NOTES']].split(", "),
            url=data_row[columns_to_position['URL']],
            created_at=data_row[columns_to_position['created_at']],
            updated_at=data_row[columns_to_position['updated_at']]
        ))
    return SubwayListSchema(subways=subways)
