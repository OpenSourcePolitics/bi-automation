from settings import *  # noqa
from http_handler import http_get, http_post
import json


def get_element_by_name(element_type, name):
    elements = http_get(f"/{element_type}")
    element_id = None
    for element in elements:
        if element["name"] == name:
            element_id = element["id"]
            break
    assert element_id
    return http_get(f"/{element_type}/{element_id}")


def get_cards_from_dashboard(dashboard_name):
    dashboard = http_get(f"/dashboard/{dashboard_name}")

    for card in dashboard["ordered_cards"]:
        metadata = card["card"]["result_metadata"]
        result = None
        if len(metadata) == 1:
            result = metadata[0]["fingerprint"]["type"]["type/Number"]["min"]
        print(card["card"]["description"] + "     " + str(result))


def get_week_result(card_id):
    payload = {
        "parameters": [
            {
                "type": "category",
                "target": [
                    "variable",
                    [
                        "template-tag",
                        "beginning_date"
                    ]
                ],
                "value": "2020-02-02"
            }
        ]
    }
    return http_post(f"/card/{card_id}/query", json=json.dumps(payload))
