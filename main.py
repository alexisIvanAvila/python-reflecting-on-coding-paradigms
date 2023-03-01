# Section 1: Functional Prompt

def flatten_and_sort(array):
    arr = []
    for element in array:
        for i in element:
            arr.append(i)
    return sorted(arr)


#How does this solution ensure data immutability?
# By alllowing elemens from the paramaterarray to be pushed into an new array

# Is this solution a pure function? Why or why not?
# yes due too the output deppending on th givven input

#Is this solution a higher order function? Why or why not?
#No because it doesnt accept more then one funtion as an argument n doesnt return it either

# Would it have been easier to solve this problem using a different programming style?
#probably not bc of how simple it is 

#Why in particular is functional programming a helpful paradigm when solving this problem?
#its helpful because we are not able to add or delete any of the elements within the array and the output (return statement purely depends on its input)

# Section 2: Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed = self.max_speed * 2