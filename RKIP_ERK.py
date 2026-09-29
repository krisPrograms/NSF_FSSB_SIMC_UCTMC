# constructs new submodels from the constants on the OG model

import random

# constant value intervals for the RKIP pathway

constants = [[0.45,0.55],[0.007,0.008],[0.6,0.65],[0.002,0.003],[0.03,0.04],
             [0.75,0.85],[0.005,0.01],[0.07,0.08],[0.9,1],[0.001,0.002],[0.8,0.9]]

num_disjoint = [3,5,7]

split1_indices = [0, 0, 0, 0, 0]
split2_indices = [706, 1028, 704, 864, 1345]
split3_indices = [75756, 34723, 99529, 67458, 79408]
split_indices = [split1_indices,split2_indices,split3_indices]


def split(rang,n):
    ranges = []
    low = rang[0]
    high = rang[1]

    split_by = (high - low) / n

    cur_low = low
    for i in range(0,n):
        cur_high = cur_low + split_by
        ranges.append([cur_low,cur_high])
        cur_low = cur_high

    return ranges


# generate random num in interval
def get_ran_value(rang):
    r = round(random.uniform(rang[0], rang[1]),5)
    return r


product_lengths = [1,2048,177147]


def main(consts,num_disjoint):
    models = {}

    for num_splits in num_disjoint:
        models[num_splits] = []

    for num_splits in num_disjoint:
        splits = []
        for intervals in consts:
            cur_split = split(intervals,num_splits)
            splits.append(cur_split)
        for i in range(0,len(splits[0])):
            count = 0
            temp = []
            for j in range(0,len(splits)):
                temp.append(splits[j][i])
                count = count + 1
            cur = models[num_splits]
            cur.append(temp)
            models[num_splits] = cur

    for key,value in models.items():
        print("Number of disjoint intervals: ", key)
        print("\n")
        for val in value:
            print("Model: ",val)
            for interval in val:
                print("Constant Interval: ", interval)
                ran = get_ran_value(interval)
                print("Constant:", ran)
            print("\n")

    return models


out = main(constants,num_disjoint)








