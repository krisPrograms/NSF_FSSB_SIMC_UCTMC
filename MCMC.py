# performs MCMC for only 3 interval submodels, writes results to a csv

import random
from matplotlib import pyplot as plt
import pymc as pm
import numpy as np
import pandas as pd
from scipy import stats
from statistics import mean
from statistics import stdev
import arviz as az
import math
log = np.log
pi = np.pi

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

means = []
sds = []
confidence_intervals = []
interval_sizes = []
distance_OG = []

def get_stats(result):
    #data = query
    mu = mean(result)
    sd = stdev(result)
    return [mu,sd]

def confidence_interval(mean,sd,n):
    conf_int = stats.norm.interval(0.95, mean, sd/math.sqrt(n))
    print(conf_int)
    return conf_int

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

def calc_difference(og, mean):
    diff = abs(og - mean)
    return diff

def mcmc(result):
    ##########################################################################

    #for result in results: only doing for 3 currently
    stat = get_stats(result)
    print('Input Gaussian {:}: μ = {}, σ = {:.2}'.format("3", stat[0], stat[1]))


    with pm.Model() as model:
        prior = pm.Normal('mu', mu=stat[0], sigma=stat[1])
        step = pm.Metropolis()

        # sample with 6 independent Markov chains
        trace = pm.sample(draws=100, chains=6, step=step, return_inferencedata=True)

    print("trace", trace)
    summary = az.summary(trace, round_to=10)
    az.plot_posterior(trace,kind="hist")
    az.plot_posterior(trace)
    plt.title("Posterior Density Estimation of the Long Run Percentage of Protein RAF1/RKIP/ERK-PP")
    plt.show()

    print(az.summary(trace, round_to=3))

    return summary


def main(query_index):
    # prepare data
    result_3 = intervals_3.loc[query_index]

    # run the MCMC
    summary = mcmc(result_3)

    cur_mean = summary["mean"][0]
    sd = summary["sd"][0]

    means.append(cur_mean)
    sds.append(sd)

    cur_int = confidence_interval(cur_mean,sd,3)
    confidence_intervals.append(cur_int)

    interval_sizes.append(cur_int[1] - cur_int[0])

    print(original.loc[query_index])
    dif = calc_difference(original.loc[query_index], cur_mean)
    distance_OG.append(dif[0])


data = {"mean": means, "standard_deviation": sds, "conf_interval": confidence_intervals,
        "distance_from_og": distance_OG, "int_size": interval_sizes}

for key,value in data.items():
    print(len(value))
df = pd.DataFrame(data)


#df.to_csv("MCMC_results_test.csv")

random.seed(100)
main(145)