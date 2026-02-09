from utils import generate_members_data

members = {
    1: "BAR001",
    2: "BAR002"
}


visits = [
    {"visit_id": "v1", "barcode": "BAR001", "reservation_id": "r1"},
    {"visit_id": "v2", "barcode": "BAR004", "reservation_id": ""},
    {"visit_id": "v3", "barcode": "BAR001", "reservation_id": "r2"}
]


def test_generate_members_data():
    members_data = generate_members_data(members, visits)
    assert members_data[1]["barcode"] == "BAR001"
    assert members_data[2]["barcode"] == "BAR002"
    assert len(members_data) == 2