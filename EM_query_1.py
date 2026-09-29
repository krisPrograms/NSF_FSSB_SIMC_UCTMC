# EM algorithm for query 3

from statistics import mean
from statistics import stdev
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from sklearn.mixture import GaussianMixture
from scipy import stats
import math
sns.set_style("white")

# read data
query_results = pd.read_csv("Query Results Final.csv")
models = query_results.columns[4:20]

# clean unneeded columns
data = query_results.drop("Query Number",axis=1)
data = data.drop("Protein",axis=1)
data = data.drop("i",axis=1)
data = data.drop("T",axis=1)
data = data.drop("Unnamed: 20",axis=1)
data = data.drop("Unnamed: 21",axis=1)

# split data by interval number
original = data[['Model 1 ']]
intervals_3 = data[["Model 2","Model 3","Model 4"]]
intervals_5 = data[["Model 5","Model 6","Model 7","Model 8","Model 9"]]
intervals_7 = data[["Model 10","Model 11","Model 12","Model 13","Model 14","Model 15", "Model 16"]]


# return distribution stats
def get_stats(result):
    #data = query
    mu = mean(result)
    sd = stdev(result)
    return [mu,sd]


# construct gaussian mixture using the EM algorithm and plot the distribution
def EM(values,num,n,line_colors):
    gmm = GaussianMixture(tol=0.000001)
    gmm.fit(np.expand_dims(values, 1))
    Gaussian_nr = 1

    x = np.linspace(min(values), max(values))  # plot the data

    for mu, sd, p in zip(gmm.means_.flatten(), np.sqrt(gmm.covariances_.flatten()), gmm.weights_):
        print('Gaussian {:}: μ = {}, σ = {:.2}, weight = {:.2}'.format(n, mu, sd, p))
        g_s = stats.norm(mu, sd).pdf(x) * p
        plt.plot(x, g_s, line_colors[num-1], label="Distribution " + str(n));
        Gaussian_nr += 1
        sns.distplot(values, bins=8, kde=False, norm_hist=True, label="{} Intervals Results".format(n))
        plt.legend()
        return [mu, sd, p]


# calculate confidence interval from EM results
def confidence_interval(mean,sd,n):
    conf_int = stats.norm.interval(0.95, mean, sd/math.sqrt(n))
    print(conf_int)
    return conf_int


# calculates the smallest confidence interval, i.e. the most precise result
def interval_difference(intervals):
    print(intervals)
    min = intervals[0][1] - intervals[0][0]
    print("Interval distance", min)
    min_index = 0

    for i in range(1,len(intervals)):
        cur_diff = intervals[i][1] - intervals[i][0]
        print("Interval distance", cur_diff)
        if cur_diff < min:
            min = cur_diff
            min_index = i + 1

    return [min_index,min]


# calculates the difference between each EM distribution mean and the original model result
def calc_difference(og, means):
    differences = []
    intervals = [3, 5, 7]

    for i in range(0, len(means)):
        diff = abs(og-means[i])[0]
        print("Difference from the original using {} intervals: {}".format(intervals[i],diff))
        differences.append(diff)

    return differences


def main(query_index, T, I, line_colors):
    ##########################################################################
    # get the needed data

    num_intervals = ["3", "5", "7"]
    num = 0
    cur_distribution = 1

    og_result = original.loc[query_index]
    result_3 = intervals_3.loc[query_index]
    result_5 = intervals_5.loc[query_index]
    result_7 = intervals_7.loc[query_index]

    results = [result_3, result_5, result_7]
    all_data = []
    means = []
    intervals = []

    ##########################################################################
    # perform the EM algorithm and plot results

    for result in results:
        stat = get_stats(result)
        print('Input Gaussian {:}: μ = {}, σ = {:.2}'.format(num_intervals[num], stat[0], stat[1]))
        values = result.array
        all_data.extend(values)
        em = EM(values,cur_distribution,num_intervals[num],line_colors)
        cur_interval = confidence_interval(em[0],em[1],int(num_intervals[num]))
        intervals.append(cur_interval)
        means.append(em[0])
        num = num+1
        cur_distribution = cur_distribution + 1

    x = np.linspace(min(all_data), max(all_data))
    plt.legend()
    #plt.title("Gaussian Distribution for the Probability of Concentration Level {} of Protein RAF1/RKIP/ERK-PP at T={}".format(I,T))
    plt.title("Gaussian Distribution for the Probability of Concentration Level {} of Protein RAF1/RKIP at T={}".format(I,T))
    plt.xlabel("Percentage Value")
    plt.ylabel("Density")
    plt.show()


    ##########################################################################
    # determine smallest confidence interval, and either plot or table
    print("Smallest Confidence Interval: ", interval_difference(intervals))
    print("")

    ##########################################################################
    # calc the difference between EM results and og result, either plot or table
    calc_difference(og_result.array, means)



# i = 0,1,3,5 for protein 1

random.seed(100)
all_indices = [[0,1,2,3,4,5], # i = 0
[6,7,8,9,10,11],#  i = 1
[18,19,20,21,22,23], # i = 3
[30,31,32,33,34,35]] # i = 5


# i = 0,1,3,5 for protein 2

#indices = [66,67,68,69,70,71]
#indices = [72,73,74,75,76,77]
#indices = [84,85,86,87,88,89]
#indices = [96,97,98,99,100,101]


T = [0,1,3,5,7,10]
I = [0,1,3,5]

line_colors = ["blue", "chocolate", "green"]

for i in range(0,len(all_indices)):  # I
    indices = all_indices[i]
    for j in range(0,len(indices)): # T
        main(indices[j], T[j], I[i], line_colors)