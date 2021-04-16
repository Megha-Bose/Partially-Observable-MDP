import numpy
import math

colour = {"Red" : 0, "Green" : 1}
num_colours = 2
states = [1, 2, 3, 4, 5, 6]
red_states = [1, 3, 6]
green_states = [2, 4, 5]
num_states = 6
action = {'L' : 0, 'R' : 1}
num_actions = 2

trans_prob = None
belief = None

x = 0.78
y = 4
rr_prob = 0.8
gg_prob = 0.95


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def initialise():
    global states, trans_prob, belief, action, colour, obs_prob
    trans_prob = numpy.zeros((num_states + 1, num_actions, num_states + 1))
    belief = numpy.zeros(num_states + 1)
    for state in states:
        if state == 1:
            trans_prob[state][action['L']][state] = x
            trans_prob[state][action['L']][state + 1] = 1 - x
            trans_prob[state][action['R']][state + 1] = x
            trans_prob[state][action['R']][state] = (1 - x)
        elif state == 6:
            trans_prob[state][action['R']][state] = x 
            trans_prob[state][action['R']][state - 1] = 1 - x
            trans_prob[state][action['L']][state - 1] = x
            trans_prob[state][action['L']][state] = (1 - x)
        else:
            trans_prob[state][action['L']][state - 1] = x
            trans_prob[state][action['L']][state + 1] = (1 - x)
            trans_prob[state][action['R']][state + 1] = x
            trans_prob[state][action['R']][state - 1] = (1 - x)
        
        if state in red_states:
            belief[state] = 1/3

    obs_prob = numpy.zeros((num_colours, num_colours))
    # prob state_colour observation 
    obs_prob[colour["Red"]][colour["Red"]] = rr_prob
    obs_prob[colour["Red"]][colour["Green"]] = 1 - rr_prob
    obs_prob[colour["Green"]][colour["Green"]] = gg_prob
    obs_prob[colour["Green"]][colour["Red"]] = 1 - gg_prob
    

def update_belief(a, o):
    global belief, action, colour, obs_prob
    new_belief = numpy.zeros(num_states + 1)
    act = action[a]
    obs = colour[o]
    sum_belief = 0
    for state in states:
        prob_st_act = 0
        for st in states:
            prob_st_act += (belief[st] * trans_prob[st][act][state])
        if state in red_states:
            new_belief[state] = (obs_prob[colour["Red"]][obs] * prob_st_act)
        else:
            new_belief[state] = (obs_prob[colour["Green"]][obs] * prob_st_act)
        sum_belief += new_belief[state]
    for state in states:
        new_belief[state] = new_belief[state] / sum_belief
    belief = new_belief

def print_belief():
    global belief
    print(belief[1:])

def initialise_output():
    global x, y
    text_file = open("2019111021_2019111011.txt", "w")
    text_file.write("2019111021 2019111011")
    text_file.write("\n%f %d" % (x, y))
    text_file.close()

def output_belief():
    global belief
    text_file = open("2019111021_2019111011.txt", "a")
    bs = [0 for _ in range(num_states)]
    for i in range(len(bs)):
        bs[i] = truncate(belief[i + 1], 4)
    text_file.write("\n%.4f %.4f %.4f %.4f %.4f %.4f" % (bs[0], bs[1], bs[2], bs[3], bs[4], bs[5]))
    text_file.close()

if __name__ == "__main__":
    initialise()
    observations = [('R', "Green"), ('L', "Red"), ('L', "Green")]
    initialise_output()
    for (act, obs) in observations:
        update_belief(act, obs)
        print_belief()
        output_belief()

    
        

