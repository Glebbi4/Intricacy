import Intricacy
import Runner

intricacy_example = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ],
    's': (0,0),
    'f': (2,2)
}

# uncomment the function print_intricacy to output the movement of the robot at each step
intricacy_runner = Runner.IntricacyRunner(intricacy_example['m'], intricacy_example['s'], intricacy_example['f']) # initialization robot
Intricacy.intricacy_controller(intricacy_runner) # call your function
print (intricacy_runner.found()) # verify that the artifact is found must be True
