from typing import List

# the output of this function is a list containing only visits with a barcode found in the members table
# invalid data is logged in a separate list, that can be returned when needed
def validate_visits_data(visits, members) -> List[dict[str, str]]:
    invalid_data = []
    valid_data = []
    for visit in visits:
        if visit["barcode"] == "" or not check_barcode(visit["barcode"], members):
            invalid_data.append(visit)
        else:
            valid_data.append(visit)
    return valid_data


# the clean members and visits tables are concatenated into one data source. the structure is a dictionary,
# where the member_id is the key, and the value is another dictionary wich has 2 keys: barcodes and the visits list
def generate_members_data(members, visits) -> dict[int, dict[str, str | list[str]]]:
    members_data = {}
    for member_id, barcode in members.items():
        members_data[member_id] = {
            "barcode": barcode,
            "visits": []
        }

    for visit in visits:
        visit_barcode = visit["barcode"]
        visit_id = visit["visit_id"]
        for member_id, data in members_data.items():
            if data["barcode"] == visit_barcode:
                data["visits"].append(visit_id)
                break

    return members_data


# check for a valid barcode in the members table
def check_barcode(barcode: str, members: dict[str, str]) -> bool:
    return barcode in members.values()

