from utils import calculate_top_members, calculate_walk_ins

members_data = {
    1: {"barcode": "BAR001", "visits": ["v1", "v2", "v3"]},
    2: {"barcode": "BAR002", "visits": ["v4"]},
    3: {"barcode": "BAR003", "visits": ["v5", "v6"]},
}

visits = [
    {"visit_id": "v1", "barcode": "BAR001", "reservation_id": ""},
    {"visit_id": "v2", "barcode": "BAR002", "reservation_id": "r1"},
    {"visit_id": "v3", "barcode": "BAR003", "reservation_id": ""},
]

def test_calculate_top_members(capsys):
    calculate_top_members(members_data)
    captured = capsys.readouterr().out

    assert "Top 5 members by number of visits:" in captured
    assert "1, 3" in captured
    assert "3, 2" in captured



def test_calculate_walk_ins(capsys):

    calculate_walk_ins(visits)

    captured = capsys.readouterr().out

    assert "Total number of walk-ins:" in captured
    assert "2" in captured