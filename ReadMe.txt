1. Run the code using Script.py
2. Make sure Statistics.py and Script.py are in the same folder/directory.
3. Statistics.py contains all the functions for calculating statistics.
4. To run a particular task uncomment the respective question/task in Script.py
5. Result Images contains images of result for each task.


FOr Task-7

1) Took the given numeric variables with their Max and Min values. For nominal variables
   assign an integer to each state. 

2) For each attribute find scale factor and offset so all values fall in the same chosen 
   range [0-1].
   -Function calc_ in statistics.py
   
3) Now you can create a 2D vector containing values of each attribute for each row.
   -Function Vec_ in statistics.py

4) Now you can compare two vectors V1 and V2 by subtracting each dimension of one from other. 
   The final calculated value [0-1] will tell how different they are.
   -Function Euclid_ or Manhatt_ in statistics.py
   
Note: For Nominal attribute, the dissimilarity value will be either 1 (Match) or 0 (No match).
      I have used an "if" loop to handle these cases in order to generate good results.
