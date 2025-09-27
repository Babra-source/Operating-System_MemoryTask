import math

def find_best_fit(job, memory_block_list):
    infinity = math.inf
    initial_memory_waste = infinity - job[2]
    subscript = 0
    counter = 1

    while counter <= len(memory_block_list):
        if job[2] > memory_block_list[counter]:
            counter += 1
        else:
            memory_waste = job[2] - memory_block_list[counter]
            if initial_memory_waste > memory_waste:
                subscript = counter
                initial_memory_waste = memory_waste
                counter += 1

    if subscript == 0:
        return 0
        # put the job in the waiting queue
    else:
        return subscript # returns the block where the job should be placed

def find_first_fit(job, memory_block_list):
    counter = 1
    while counter < len(memory_block_list):
        if job[2] > memory_block_list[counter-1]:
            counter += 1
        else:
            return counter # returns the appropriate block number

    return 0 # when the function returns a zero, then no match was found