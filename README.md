
# Statistical Inference for Model Checking of Uncertain Continuous-Time Markov Chains
Takes an uncertain discrete time Markov Chain model (IDTMC) and constructs continuous-time Markov chain (CTMC) submodels. All models constructed from the RKIP-inhibited ERK pathway are stored in the "Models" folder, but the user can also create their own for analysis. "RKIP_ERK_Properties" holds the queries used for RKIP-inhibited ERK pathway analysis, but the user can also create their own. 

### Dependencies
* Please utilize the following commands for dependency installations:
  * pip install pandas
  * pip install seaborn
  * pip install matplotlib 
  * pip install numpy
  * pip install sklearn
  * pip install scipy
  * pip install pymc 
  * pip install arviz
  
* You will also need to download the following applications:
  * Anaconda
  * PRISM Model Checker 4.8.1
    * Be sure the version matches your Python installation
    
### Directions 
1. In 'RKIP_ERK.py', replace "num_disjoint" with the desired number of disjoint subintervals. Also, replace the "constants" list with the desired interval probability ranges. 

2. Run 'RKIP_ERK.py' to construct new submodels. The transitions of the newly constructed submodels are printed to the console. Information is printed line by line with the new probability intervals followed by the randomly selected probabilities.  

3. Using the model information from 'RKIP_ERK.py', construct the corresponding PRISM model files. Or, the user can use the pre-existing models in the "Models' Folder. 

4. Write a PRISM properties file containing the desired queries to be evaluated, or use the  provided 'RKIP_ERK_Properties' file. Evaluate the queries on all submodel files. Do the same for the original PRISM model (the model before uncertainty was introduced). If the user is replicating the paper results using 'RKIP_ERK_Properties', the results are already provided in the main directory as 'Query Results Final.csv'. If the user is using their own properties file, store the query results in a csv file with the name 'Query Results Final.csv' in the same structure as the provided 'Query Results Final.csv' file. Ensure that this file is saved in the same folder as 'EM_query_1.py','EM_query_2.py', 'EM_query_3.py', and 'MCMC.py'. Do not save the new results in the 'Results' folder.  

5. Plot the query results using 'query_plots.py'. The user can change plot titles using plt.title("") as needed. 

6. Run the Expectation-Maximization (EM) algorithm on the query results using 'EM_query_1.py','EM_query_2.py', and 'EM_query_3.py'. These files print the EM results to the console and also plot the resulting distribution. The user can change plot titles using plt.title("") as needed. 

7. Run a Markov chain Monte Carlo (MCMC) simulation using 'MCMC.py'. This file prints the MCMC results to the console and also plots the resulting distribution. The user can change plot titles using plt.title("") as needed. Results are printed to the console, but can also be written to a csv file by uncommenting df.to_csv("MCMC_results_all.csv"). 

8. Steps 6 and 7 return the parameters (mean and standard deviation) of the approximated probability distributions using EM and MCMC respectively. For each set of parameters, calculate the difference between the approximated means and the query results from the original model. The smaller the difference between the results, the more accurate the statistical algorithm was in approximating model performance in the face of uncertainty. 

Final results for this paper are recorded in 'CTMC_All_Results_Stats.csv'. This file includes the approximated probability distributions for all queries on both proteins using the EM and MCMC algorithms. The difference between the approximate probability distribution and the original model is also recorded. Further, the approximated probability distributions that fall below the average difference from the original model are identified.  


 
### Citation Sparks, Hailey, and Krishnendu Ghosh. "Statistical Inference and Probabilistic Model Checking on Uncertain Continuous-Time Markov Chains Representing Biochemical Pathways." In BIOSTEC (2), pp. 505-516. 2026.  
### Acknowledgement: NSF CCF Award # 2227898

