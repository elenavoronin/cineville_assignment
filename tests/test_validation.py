from validation import validate_visits_data, check_barcode


members = {
    1: "BAR001",
    2: "BAR002"
}


visits = [
    {"visit_id": "v1", "barcode": "BAR001", "reservation_id": "r1"},
    {"visit_id": "v2", "barcode": "BAR004", "reservation_id": ""},
    {"visit_id": "v3", "barcode": "BAR001", "reservation_id": "r2"}
]


def test_barcode_validation():

    assert check_barcode(visits[0]["barcode"], members) == True
    assert check_barcode( visits[1]["barcode"], members) == False

    valid_visits, invalid_visits = validate_visits_data(visits, members)
    assert valid_visits[0]["visit_id"] == "v1"
    assert valid_visits[1]["visit_id"] == "v3"
    assert invalid_visits[0]["barcode"] == "BAR004"

