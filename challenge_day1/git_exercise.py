from maja import get_name as name1
from martyna import string_name as name2, paragraph1
from Vincent import name as name3, paragraph1_c
from eryk import name_eryk as name4, paragraph1b

def funct():
    print(f"This is CarPark. We are {name1()}, {name2()}, {name3()}, {name4()}.\n")
    story = paragraph1(), paragraph1b(), paragraph1_c()
    return story
funct()
