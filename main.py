import random

num_of_test = 5

def calc_drops(frames_list:list[int], fps:int, interval_len:int):
    interval_len *= 1000 #interval len given in sec, we convert to ms
    max_len_drop, counter_total_drops, sequential_counter_events, last_lonely_drop_time = 0, 0, 0, 0
    first_drop_time, last_drop_time, first_drop_index, last_drop_index, interval_violation_counter = 0, 0, 0, 0, 0
    #the index for the first and the last drop is the last index of a frame found in the list before the drop
    min_len_drop_sequence = float("inf")
    for index in range(len(frames_list) - 1):
        num_of_drops = ((frames_list[index + 1] - frames_list[index]) // (1000 // fps)) - 1 # check if 1/fps is true
        if num_of_drops == 0:
            continue
        #one drop and the first one
        first_drop_time = (counter_total_drops == 0) * (frames_list[index] + (1000 // fps)) + first_drop_time
        first_drop_index = ((counter_total_drops == 0) * index) + first_drop_index

        interval_violation_counter = interval_violation_counter + (num_of_drops == 1) *\
                                     (frames_list[index] - last_lonely_drop_time < interval_len) * (not first_drop_time == 0)
        last_lonely_drop_time = (num_of_drops == 1) * frames_list[index] + (not num_of_drops == 1) * last_lonely_drop_time

        #adding the amount of drops that we found
        counter_total_drops += num_of_drops
        #updating the last drop as long as we go over the list
        last_drop_time = frames_list[index + 1] - (1000 // fps)
        last_drop_index = index
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
          f"first_drop_time = {first_drop_time}\n", f"first_drop_index = {first_drop_index}\n",f"last_drop_time = {last_drop_time}\n",
          f"last_drop_index = {last_drop_index}\n", f"interval_violation_counter = {interval_violation_counter}\n")


if __name__ == '__main__':
    print(f"Running {num_of_test} tests:")
    for test_no in range(num_of_test):
        current_fps = random.randint(30 ,45)
        interval_len = 1 / random.randint(1, 4)
        test_list = []
        for num in range(25000, 25000 + (1000 // current_fps) * 15, (1000 // current_fps)):
            if random.randint(0,1):
                test_list.append(num)
        if len(test_list) == 0:
            print("len is zero") # for debugging
        else:
            print(f"for tests list {test_list}, fps={current_fps} and interval len={interval_len} the output is:\n")
            calc_drops(test_list, current_fps, interval_len)
            print("-" * 100)
    print("Thank you for your time (:")

