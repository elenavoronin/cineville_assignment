from typing import List
import sys

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
    return valid_data, invalid_data

# check for a valid barcode in the members table
def check_barcode(barcode: str, members: dict[str, str]) -> bool:
    return barcode in members.values()

