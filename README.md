# Scenario-Software
 Doing consistency analysis and clustering for Scenario analysis
 
 # How To
 1. Create a xlsx-list of relevant factors (key factors) that describe the field under scrutiny and their possible future developments (projections). It must be in the form of "SimpleTest_Factors.xlsx"
 2. Run Step1.py with this file. It creates a consistency matrix for you to fill out by rating the pairwise consistency of the future projections
 3. After filling out the matrix, run Step2.py! It will iterate through every possible combination of projections, keeping the a variable number n of the most consistent. Afterwards it will run a hierarchical cluster algorithm by using the Hamming-Metric
 4. The programm will present you a choice of how many clusters to keep. You should make the decision based on your resources of how many scenarios are reasonable and the distance in the last clustering steps. The bigger the distance, the more likely you should make a cut there.
 5. The programm will create a file called clusters.xlsx which contains the choosen number of clusters and the composition of projections in each cluster
 6. Afterwards the programm will run multidimensional scaling algorithm to visualize the clusters
 
 
 
 
 There is much to do in the code, like adding comments, structuring, moving all adjunsting screws to a single file, working on a GUI, increasing performance, optimizing the multidimensional scaling, and so on...
 For this, please refer to Selbstreflektion.jpg
