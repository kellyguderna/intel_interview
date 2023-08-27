import random

num_of_test = 5


def calc_drops(frames_list:list[int], fps:int):
    max_len_drop = 0
    min_len_drop_sequence = float("inf")
    counter_total_drops = 0
    sequential_counter_events = 0
    first_drop_time = 0
    last_drop_time = 0
    #ask what is the interval, ask what to return in first and last - the time they were missing ?
    for index in range(len(frames_list) - 1):
        num_of_drops = ((frames_list[index + 1] - frames_list[index]) // (1000 / fps)) - 1 # check if 1/fps is true
        if num_of_drops == 0:
            continue
        #one drop and the first one
        first_drop_time = (counter_total_drops == 0) * (frames_list[index] + (1000 // fps)) + first_drop_time
        #adding the amount of drops that we found
        counter_total_drops += num_of_drops
        #updating the last drop as long as we go over the list
        last_drop_time = frames_list[index + 1] - (1000 // fps)
        #adding events that bigger than one drop
        sequential_counter_events = (num_of_drops > 1) + sequential_counter_events
        #finding the biggest sequence
        max_len_drop = max(max_len_drop, num_of_drops)
        #finding the minimum sequence that is bigger than one
        if num_of_drops > 1:
            min_len_drop_sequence = min(num_of_drops, min_len_drop_sequence)

    drop_percentage = round((counter_total_drops / (counter_total_drops + len(frames_list))) * 100, 2)
    print(f" counter_total_drops = {int(counter_total_drops)}\n",f"drop_percentage = {drop_percentage}%\n",
          f"sequential_counter_events = {sequential_counter_events}\n",f"max_len_drop = {int(max_len_drop)}\n",
          f"min_len_drop_sequence = {int(min_len_drop_sequence) if not min_len_drop_sequence == float('inf') else 0}\n",
          f"first_drop_time = {first_drop_time}\n",f"last_drop_time = {last_drop_time}\n")  #interval


if __name__ == '__main__':
    print(f"Running {num_of_test} tests:")
    for test_no in range(num_of_test):
        current_fps = random.randint(30 ,45)
        test_list = []
        for num in range(25000, 25000 + (1000 // current_fps) * 15, (1000 // current_fps)):
            if random.randint(0,1):
                test_list.append(num)
        if len(test_list) == 0:
            print("len is zero") # for debugging
        else:
            print(f"for tests list {test_list} and for fps={current_fps} the output is:\n")
            calc_drops(test_list, current_fps)
            print("-" * 100)
    print("Thank you for your time (:")
