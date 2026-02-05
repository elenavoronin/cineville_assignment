from typing import List

# The members dictionary uses the member id as the key and the value equals their cineville card barcode
def read_members_file() -> dict[int, int]:
    members = {}
    with open("./data/members.csv") as members_file:
        next(members_file)
        for line in members_file:
            line_split = line.strip().split(",") or [""]
            members[int(line_split[0])]=line_split[1]
    return members

# The visits are now mapped into a list of dictionaries. Each item in the list is a dictionary containing
# the visit_id, the barcode and the reservation_id.
def read_visits_file() -> List[dict[str, str]]:
    visits = []
    with open("./data/visits.csv") as visits_file:
        next(visits_file)
        for line in visits_file:
            line_split = line.strip().split(",") or [""]
            visits.append({
                "visit_id": line_split[0],
                "barcode": line_split[1],
                "reservation_id": line_split[2]
            })
    return visits
