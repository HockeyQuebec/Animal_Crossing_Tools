from encodings import utf_8

from fuzzysearch import find_near_matches_in_file, find_near_matches

fish = input("What fish?")
print('\n')
with open('fish.txt', 'r') as f:
    for line in f:

        stripped = line.strip()
        match = find_near_matches(fish, stripped, max_l_dist=0)
        if match:
            print(stripped)
