import random
opt = [1, 2, 3, 4, 5, 6]
def generate_random_tubes():
    colors = ['yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green']
    random.shuffle(colors)

    
    tube1 = colors[:3]
    tube2 = colors[3:6]
    tube3 = colors[6:9]
    tube4 = colors[9:12]
    tube5 = []
    tube6 = []    
    tubes = [tube1, tube2, tube3, tube4, tube5, tube6]
    random.shuffle(tubes)   
    return tubes

def get_valid_tube_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num in opt:
                return num
            else:
                print("Invalid choice. Please select 1, 2, 3, 4, 5 or 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def pouring(pickl=list, pourl=list):
    col = pickl[-1]
    pickl.pop()
    pourl.append(col)

def print_all(all=list):
    n = 1
    for i in all:
        print("Tube : ",n, i)
        n+=1

def checking(poured=list):
    if len(poured) == 3:
        pod = set(poured)
        if len(pod) == 1:
            return True

def print_initial_State():
    all_tubes = generate_random_tubes()
    tube1, tube2, tube3, tube4, tube5, tube6 = all_tubes

    print("Initial state:")
    print("1 :", tube1) 
    print("2 :", tube2) 
    print("3 :", tube3) 
    print("4 :", tube4)
    print("5 :", tube5) 
    print("6 :", tube6)

    return all_tubes

