from typing import List

def read_integers() -> List[int]:
    numbers = input()
    numbers_list = numbers.split(",")
    
    int_list = []
    for s in numbers_list:
        int_list.append(int(s))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
