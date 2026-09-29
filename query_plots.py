# used to plot all queries

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme(style="whitegrid", palette="dark")

# read data
query_results = pd.read_csv("Query Results Final.csv")
data = query_results.drop("Unnamed: 20",axis=1)
data = data.drop("Unnamed: 21",axis=1)
models = query_results.columns[4:20]
original = data[['Model 1 ']]
intervals_3 = data[["Model 2","Model 3","Model 4"]]
intervals_5 = data[["Model 5","Model 6","Model 7","Model 8","Model 9"]]
intervals_7 = data[["Model 10","Model 11","Model 12","Model 13","Model 14","Model 15", "Model 16"]]

print(data.head())

# plots for 1 at i = 0 [2,7], 3, 5, 7 at T = 0,3,5,7,10

# protein 1

def query_1(data, set_indices, ylabel, line_types, line_colors, Is):
    t = [0, 1, 3, 5, 7, 10]
    y_points = []
    columns = data.columns
    line = 0
    model_num = 1

    for i in range(0, len(columns)):
        # this is the current model
        cur_column = columns[i]

        # this is the current i level
        for indices in set_indices:
            cur_i = Is[line]
            for index in indices:
                cur_data = data[cur_column]
                y_points.append(cur_data.loc[index])
            sns.lineplot(x=t, y=y_points, linestyle=line_types[line], label="Model {}, i level {}".format(model_num, Is[line]), linewidth=1, legend = False)
            y_points = []
            line = line + 1
        model_num = model_num+1
        line = 0

    #plt.legend(loc='upper center', ncol=6)
    plt.xlabel("Time", fontsize="medium")
    plt.ylabel(ylabel, fontsize="medium")
    #plt.title("Probability of level i concentration of RAF1/RKIP/ERK-PP at time T")
    plt.title("Probability of level i concentration of RAF1/RKIP at time T")
    plt.show()


# i = 0 [8,13]

# for 3 intervals
protein1_indices = [[0,1,2,3,4,5], [6,7,8,9,10,11], [18,19,20,21,22,23], [30,31,32,33,34,35]]
Is = [0,1,3,5]
line_colors = ["blue","orange","green"]
line_types = ["-","--",'-.',':']
query_1(intervals_3, protein1_indices,"Probability of level i",line_types,line_colors,Is)

# for 5 intervals
query_1(intervals_5, protein1_indices,"Probability of level i",line_types,line_colors,Is)

# for 7 intervals

query_1(intervals_7, protein1_indices,"Probability of level i",line_types,line_colors,Is)

# protein 2

protein2_indices = [[66,67,68,69,70,71], [72,73,74,75,76,77], [84,85,86,86,88,89], [96,97,98,99,100,101]]

# 3 intervals

query_1(intervals_3, protein1_indices,"Probability of level i",line_types,line_colors,Is)

# 5 intervals

query_1(intervals_5, protein1_indices,"Probability of level i",line_types,line_colors,Is)

# 6 intervals

query_1(intervals_7, protein1_indices,"Probability of level i",line_types,line_colors,Is)


# plots for 2 at T=0,3,5,7,10

def query_2(data, indices,ylabel):
    t = [0,1,3,5,7,10]
    y_points = []
    columns = data.columns

    for i in range(0,len(columns)):
        cur_column =columns[i]
        for index in indices:
            cur_data = data[cur_column]
            y_points.append(cur_data.loc[index])
        print(y_points)
        sns.lineplot(x=t, y=y_points, label="Model {}".format(i+1), linewidth=2,legend = False)
        y_points = []
    plt.legend(loc='upper right', ncol=3)
    plt.xlabel("Time", fontsize="medium")
    plt.title("Expected Percentage of RAF1/RKIP at time T")
    plt.ylabel(ylabel, fontsize="medium")
    plt.show()


# protein 1 [132, 137]
query_2(intervals_3,[132,133,134,135,136,137],"Percentage of Protein RAF1/RKIP")
query_2(intervals_5,[132,133,134,135,136,137],"Percentage of Protein RAF1/RKIP")
query_2(intervals_7,[132,133,134,135,136,137],"Percentage of Protein RAF1/RKIP")

# protein 2 [138,143]




def query_3(index,ylabel):
    # 3 intervals
    sns.lineplot(x=[1, 2, 3], y=intervals_3.loc[index], label="3 Intervals", linewidth=2)
    # 5 intervals
    sns.lineplot(x=[1, 2, 3, 4, 5], y=intervals_5.loc[index], label="5 Intervals", linewidth=2)
    # 7 intervals
    sns.lineplot(x=[1, 2, 3, 4, 5, 6, 7], y=intervals_7.loc[index], label="7 Intervals", linewidth=2)
    plt.legend()
    plt.xlabel("Submodel Number", fontsize="medium")
    plt.ylabel(ylabel, fontsize="medium")
    plt.title("Expected Long-run Percentage of Protein RAF1/RKIP")
    plt.show()


# plots for 3

# protein 1, index 144

query_3(144,"Long Run Percentage of Protein RAF1/RKIP")

# protein 2, index 145

query_3(145,"Long Run Percentage of Protein RAF1/RKIP/ERK-PP")




