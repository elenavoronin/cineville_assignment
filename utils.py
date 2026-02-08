import csv

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

# export data to a csv file
def export_to_csv(result):
    with open("./data/result.csv", "w", newline="") as file:
        file_writer = csv.writer(file)
        file_writer.writerow(['member_id', 'barcode', 'visits'])

        for member_id, data in result.items():
            file_writer.writerow([
                member_id,
                data["barcode"],
                ", ".join(data["visits"])
              ])

# prints top 5 members by visits
def calculate_top_members(members_data):
    top_members = []

    members_data_sorted = sorted(members_data.items(),
                                 key=lambda x: len(x[1]["visits"]),
                                 reverse=True)

    print("Top 5 members by number of visits:")
    for member_id, member_info in members_data_sorted[:5]:
        print(f"{member_id}, {len(member_info['visits'])}")


# prints total number of visits without a reservation
def calculate_walk_ins(visits):
     print("Total number of walk-ins:")
     walk_ins = [visit for visit in visits if visit["reservation_id"] == ""]
     print(len(walk_ins))




