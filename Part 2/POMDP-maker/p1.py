import numpy as np
import sys

discount = 0.5
values = "reward"

actions = np.array(["stay", "up", "down", "left", "right"])
observations = np.array(['o1', 'o2', 'o3', 'o4', 'o5', 'o6'])

# m x n grid
m = 2
n = 4

target_move_prob = 0.1
target_stay_prob = 0.6
target_call_on_prob = 0.5
target_call_off_prob = 0.1

roll_number = 2019111021
x = 1 - (((roll_number % 10000) % 30 + 1) / 100)

step_cost = -1
track_reward = (roll_number) % 90 + 10

agent_move_prob = x

start_target_x = 1
start_target_y = 0


def get_state(x1, y1, x2, y2, c):
    return 's_(' + str(x1)+','+str(y1)+')_('+str(x2)+','+str(y2)+')_'+str(c)


def get_observation(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        obs = "o1"
    elif x1 == x2 - 1 and y1 == y2:
        obs = "o2"
    elif x1 == x2 and y1 == y2 + 1:
        obs = "o3"
    elif x1 == x2 + 1 and y1 == y2:
        obs = "o4"
    elif x1 == x2 and y1 == y2 - 1:
        obs = "o5"
    else:
        obs = "o6"
    return obs


def print_discount():
    global discount
    print("discount: {0}".format(discount))


def print_values():
    global values
    print("values: {0}".format(values))


def print_states():
    global m, n
    print("states: ", end="")
    for agent_x in range(0, n):
        for agent_y in range(0, m):
            for target_x in range(0, n):
                for target_y in range(0, m):
                    for call in range(0, 2):
                        state = get_state(agent_x, agent_y, target_x, target_y, call)
                        print(state, end=" ")
    print("")


def print_actions():
    global actions
    print("actions: ", end="")
    for act in actions:
        print(act, end=" ")
    print("")


def print_observations():
    global observations
    print("observations: ", end="")
    for obs in observations:
        print(obs, end=" ")
    print("")


def print_start_states():
    global m, n, start_target_x, start_target_y
    print("start include: ", end="")
    for agent_x in range(0, n): 
        for agent_y in range(0, m):
            target_x = start_target_x
            target_y = start_target_y
            for call in range(0, 2):
                obs = get_observation(agent_x, agent_y, target_x, target_y)
                if obs == "o6":
                    state = get_state(agent_x, agent_y, target_x, target_y, call)
                    print(state, end=" ")
    print("")


def move_agent(x, y, action):


def move_target(x, y):



def print_transition(agent_x, agent_y, target_x, target_y, call, action):
    start_state = get_state(agent_x, agent_y, target_x, target_y, call)
    agent_next_pos, agent_prob = move_agent(agent_x, agent_y, action)
    agent_nxt_len = len(agent_pos)
    for i in range(agent_nxt_len):
        for next_call in range(0, 2):
            call_prob = 0

            # Todo

            target_next_pos, target_prob = move_target(target_x, target_y)
            
            target_nxt_len = len(target_pos)

            for j in range(target_nxt_len)):
                total_prob = agent_prob[i] * target_prob[j] * call_prob
                end_state = get_state(agent_pos[i][0], agent_pos[i][1], target_pos[i][0], target_pos[i][1], next_call)

                print("T: {0} : {1} : {2} {3}".format(action, start_state, end_state, total_prob))



def print_transition_matrix():
    global actions, m, n
    for action in actions:
        for agent_x in range(0, n):
            for agent_y in range(0, m):
                for target_x in range(0, n):
                    for target_y in range(0, m):
                        for call in range(0, 2):
                            print_transition(agent_x, agent_y, target_x, target_y, call, action)
                            

def print_observation_probs():
    global m, n
    for agent_x in range(0, n):
        for agent_y in range(0, m):
            for target_x in range(0, n):
                for target_y in range(0, m):
                    for call in range(0, 2):
                        end_state = get_state(agent_x, agent_y, target_x, target_y, call)
                        obs = get_observation(agent_x, agent_y, target_x, target_y)

                        print("O: * : {0} : {1} 1.0".format(end_state, obs))


def print_rewards():
    global actions, m, n
    for action in actions:
        for agent_x in range(0, n):
            for agent_y in range(0, m):
                for target_x in range(0, n):
                    for target_y in range(0, m):
                        for call in range(0, 2):
                            end_state = get_state(agent_x, agent_y, target_x, target_y, call)
                            if agent_x == target_x and agent_y == target_y and call == 1:
                                print("R: {0} : * : {1} : * {2}".format(action, end_state, track_reward))
                            elif action != "stay":
                                print("R: {0} : * : {1} : * {2}".format(action, end_state, step_cost))



def print_pomdp():
    print_discount()
    print_values()
    print_states()
    print_actions()
    print_observations()
    print_start_states()
    print_transition_matrix()
    print_observation_probs()
    print_rewards()


if __name__ == "__main__":
    sys.stdout = open('../POMDP/p1.pomdp', 'w')
    print_pomdp()
    sys.stdout.close()