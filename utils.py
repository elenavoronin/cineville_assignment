import csv

# export data to a csv file
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




