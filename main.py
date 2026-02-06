from read_files import read_members_file, read_visits_file
from validation import validate_visits_data, generate_members_data
from utils import export_to_csv, calculate_top_members, calculate_walk_ins


def main():
    members = read_members_file()
    visits = read_visits_file()
    validated_visits = validate_visits_data(visits, members)
    final_result = generate_members_data(members, validated_visits)
    export_to_csv(final_result)
    calculate_top_members(final_result)
    calculate_walk_ins(validated_visits)

if __name__=="__main__":
    main()
