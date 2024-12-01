def read_loc_lists(file_name: str) -> tuple[list]:
    """
    The two Elves groups sent you the lists of the locations
      they read in the Chief Historians notes.
    This functions returns the two lists
    """
    with open(file_name) as f:
        loc_list = f.readlines()

    # Get lists
    loc_list1 = list()
    loc_list2 = list()
    for pair in loc_list:
        split = pair.split(" ")
        loc_list1.append(int(split[0]))
        loc_list2.append(int(split[-1]))

    return loc_list1, loc_list2


def calculate_distance(list1: list, list2: list) -> int:
    """
    Part 1
    They want to know how far apart the two lists are.
    """
    distance = 0
    for loc_id1, loc_id2 in zip(list1, list2):
        distance += abs(loc_id1 - loc_id2)

    return distance


def calculate_similarity_score(list1: list, list2: list) -> int:
    """
    Part 2
    They think they could have added locations ID that are the same
      and want to know how similar the two lists are.
    """
    similarity_score = 0
    for loc_id1 in list1:
        frequency = list2.count(loc_id1)
        similarity_score += loc_id1 * frequency
    
    return similarity_score


def main():
    # Read input lists
    input_lists = "01/input.csv"
    left_list, right_list = read_loc_lists(input_lists)

    # Sort lists
    left_list.sort()
    right_list.sort()

    # Part 1 - Calculate distance
    distance = calculate_distance(left_list, right_list)
    print(f"The distance is: {distance}")

    # Part 2 - Similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score is: {similarity_score}")


if __name__ == "__main__":
    main()
