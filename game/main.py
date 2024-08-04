import random
from functions import pouring, print_all, checking, get_valid_tube_number, print_initial_State

all_tubes = print_initial_State()

done = 0
checkL = []
while done < 4:        
    pick_index = get_valid_tube_number("Select the test-tube (1/2/3/4/5/6) you want to pick: ") - 1
    pick = all_tubes[pick_index]

    while len(pick) == 0 or pick in checkL:
        print(f"Cannot pick test-tube {pick_index + 1} (empty or already checked).")
        pick_index = get_valid_tube_number("Select another test-tube (1/2/3/4/5/6) you want to pick: ") - 1
        pick = all_tubes[pick_index]

    print("You picked:", pick)

    pour_index = get_valid_tube_number("Select the test-tube (1/2/3/4/5/6) you want to pour into: ") - 1
    pour = all_tubes[pour_index]

    while pick == pour or len(pour) == 3 or (pour != [] and pick[-1] != pour[-1]):
        if pick == pour:
            print("You can't pour into the same test-tube.")
        if len(pour) == 3:
            print(f"Test-tube {pour_index + 1} is full.")
        if (pour != [] and pick[-1] != pour[-1]):
            print("You can't over another color.")    
        pour_index = get_valid_tube_number("Select another test-tube (1/2/3/4/5/6) you want to pour into: ") - 1
        pour = all_tubes[pour_index]

    print("You want to pour into:", pour)
    
    pouring(pick, pour)
    if checking(pour):
        done += 1
        checkL.append(pour)

    print_all(all_tubes)

print("You won!")
