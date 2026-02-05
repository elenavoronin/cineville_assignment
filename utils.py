import csv
from itertools import count
from typing import List


def export_to_csv(result):
    with open("./data/result.csv", "w", newline="") as file:
        file_writer = csv.writer(file)
        file_writer.writerow(['member_id', 'barcode', 'visits'])

        for member_id, data in result.items():
            file_writer.writerow([
                member_id,
                data["barcode"],
                data["visits"]
              ])

def calculate_top_members(members_data) -> List[int]:
    top_members = []
    for member in members_data:
        member["visit_count"] = len(member["visits"])

    members_data_sorted = sorted(members_data.items(),
                                 key=lambda x: len(x["visits"]),
                                 reverse=True)

    for member_id, data in members_data_sorted.items():
        top_members[member_id] = data["visit_count"]

    print(top_members)
    return top_members


# def calculate_walk_ins(members_data) -> int:
#     return members_data.values()
#
#
#
# def print_bonus_result():
#
