import csv
from Statistics import mean_, std_, var_, Cov_, Cor_,  calc_, Vec_, Hist_, Euclid_, Manhatt_
import math

# For Boxplot, Scatterplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# For Nominal variables
import pandas
from collections import Counter



#------------------------------------------------------------------------------------
# Taking Input

filename="student-por.csv"
fields= []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        rows.append(row)
        
Fedu = [int(row[0]) for row in rows]
Mjob = [(row[1]) for row in rows]
reason = [(row[2]) for row in rows]
studytime = [int(row[3]) for row in rows]
failures = [int(row[4]) for row in rows]
goout = [int(row[5]) for row in rows]
absences = [int(row[6]) for row in rows]
G1 = [int(row[7]) for row in rows]
G2 = [int(row[8]) for row in rows]
G3 = [int(row[9]) for row in rows]



#------------------------------------------------------------------------------------        
# Print the first 5 rows of CSV
"""     
print("Total no. of rows: %d"%(csvreader.line_num)) 
print('Field names are:' + ', '.join(field for field in fields)) 
  
print('First 5 rows are:\n') 
for row in rows[:5]:
    for col in row: 
        print("%s"%col, end =" ")
    print('\n') 
    
"""
#------------------------------------------------------------------------------------
"""
# Question-1
print("\n")
print("Mean G1: %.6f" %mean_(G1))
print("Mean G2: %.6f" %mean_(G2))
print("Mean G3: %.6f" %mean_(G3))

print("\n")
print("Standard deviation G1: %.6f" %std_(G1))
print("Standard deviation G2: %.6f" %std_(G2))
print("Standard deviation G3: %.6f" %std_(G3))
print("\n")

"""
#------------------------------------------------------------------------------------
"""
# Question-2
CovM = []
Co1 = []
Co2 =[]
Co3 =[]
Co1.append(Cov_(G1, G1))
Co1.append(Cov_(G1, G2))
Co1.append(Cov_(G1, G3))

Co2.append(Cov_(G2, G1))
Co2.append(Cov_(G2, G2))
Co2.append(Cov_(G2, G3))

Co3.append(Cov_(G3, G1))
Co3.append(Cov_(G3, G2))
Co3.append(Cov_(G3, G3))


CovM.append(Co1)
CovM.append(Co2)
CovM.append(Co3)
print("\n")
print("Covariance Matrix: \n")
for i in range(3):
    for j in range(3):
        print("%.6f"%CovM[i][j], end=" ")
    print("\n")

Cor = []
Cor.append(Cor_(G1, G2));
Cor.append(Cor_(G2, G3));
Cor.append(Cor_(G1, G3));

print("Correlation G1, G2: %.6f"%Cor[0])
print("Correlation G2, G3: %.6f"%Cor[1])
print("Correlation G1, G3: %.6f"%Cor[2])
print("\n")

"""
#------------------------------------------------------------------------------------
"""
# Question-3

colors = (1,0,0)
area = math.pi*3
plt.scatter(G1, G2, s=area, c=colors, alpha=0.5)
plt.title('a) G1 and G2')
plt.xlabel('G1')
plt.ylabel('G2')
plt.show()

colors = (0,1,0)
plt.scatter(G2, G3, s=area, c=colors, alpha=0.5)
plt.title('b) G2 and G3')
plt.xlabel('G2')
plt.ylabel('G3')
plt.show()

colors = (0,0,1)
plt.scatter(G1, G3, s=area, c=colors, alpha=0.5)
plt.title('c) G1 and G3')
plt.xlabel('G1')
plt.ylabel('G3')
plt.show()
"""
#------------------------------------------------------------------------------------
"""
# Question -4

bin_edges = [0, 1, 2, 3, 4]
plt.hist(Fedu, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Father Education")
plt.ylabel("Number of students")
plt.show()

letter_counts = Counter(Mjob)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar', legend =False)
plt.show()

bin_edges = [1, 2, 3, 4]
plt.hist(studytime, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Weekly Study Time")
plt.ylabel("Number of students")
plt.show()

bin_edges = [1, 2, 3]
plt.hist(failures, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("No. of past class failures")
plt.ylabel("Number of students")
plt.show()

bin_edges = [1, 2, 3, 4, 5]
plt.hist(goout, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Going out with friends")
plt.ylabel("Number of students")
plt.show()


Fedu1 = [int(row[0]) for row in rows if int(row[9])>12]
Mjob1 = [(row[1]) for row in rows  if int(row[9])>12]
studytime1 = [int(row[3]) for row in rows if int(row[9])>12]
failures1 = [int(row[4]) for row in rows if int(row[9])>12]
goout1 = [int(row[5]) for row in rows if int(row[9])>12]

bin_edges = [0, 1, 2, 3, 4]
plt.hist(Fedu1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Father Education")
plt.ylabel("Number of students")
plt.show()


letter_counts = Counter(Mjob1)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar', legend =False)
plt.show()


plt.hist(studytime1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Weekly Study Time")
plt.ylabel("Number of students")
plt.show()


plt.hist(failures1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("No. of past class failures")
plt.ylabel("Number of students")
plt.show()


plt.hist(goout1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Going out with friends")
plt.ylabel("Number of students")
plt.show()


Fedu1 = [int(row[0]) for row in rows if int(row[9])<=12]
Mjob1 = [(row[1]) for row in rows  if int(row[9])<=12]
studytime1 = [int(row[3]) for row in rows if int(row[9])<=12]
failures1 = [int(row[4]) for row in rows if int(row[9])<=12]
goout1 = [int(row[5]) for row in rows if int(row[9])<=12]


plt.hist(Fedu1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Father Education")
plt.ylabel("Number of students")
plt.show()


letter_counts = Counter(Mjob1)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar', legend =False)
plt.show()


plt.hist(studytime1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Weekly Study Time")
plt.ylabel("Number of students")
plt.show()


plt.hist(failures1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("No. of past class failures")
plt.ylabel("Number of students")
plt.show()

plt.hist(goout1, rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Going out with friends")
plt.ylabel("Number of students")
plt.show()
"""
#------------------------------------------------------------------------------------
"""
# Question-5
plt.boxplot(absences, sym='k.')
plt.title("Boxplot")
plt.ylabel("Number of school absences")
plt.show()

plt.boxplot(G1, sym='k.')
plt.title("Boxplot")
plt.ylabel("First period grade")
plt.show()

plt.boxplot(G2, sym='k.')
plt.title("Boxplot")
plt.ylabel("Second period grade")
plt.show()

plt.boxplot(G3, sym='k.')
plt.title("Boxplot")
plt.ylabel("Final Grade")
plt.show()

"""
#------------------------------------------------------------------------------------
"""
# Question-6

colors = (1,0,0)
area = math.pi*3
plt.scatter(G3, studytime, s=area, c=colors, alpha=0.5)
plt.title('a) G3 and studytime')
plt.xlabel('G3')
plt.ylabel('studytime')
plt.show()

colors = (0,1,0)
plt.scatter(G3, failures, s=area, c=colors, alpha=0.5)
plt.title('b) G3 and failures')
plt.xlabel('G3')
plt.ylabel('failures')
plt.show()

colors = (0,0,1)
plt.scatter(G3, goout, s=area, c=colors, alpha=0.5)
plt.title('c) G3 and goout')
plt.xlabel('G3')
plt.ylabel('goout')
plt.show()

colors = (0,0,0)
plt.scatter(G3, absences, s=area, c=colors, alpha=0.5)
plt.title('d) G3 and absences')
plt.xlabel('G3')
plt.ylabel('absences')
plt.show()

"""
#------------------------------------------------------------------------------------

#Question-7
"""
S, O = calc_()
Vecs = Vec_(S, O, rows[:10])
DisM=[]
for i in range(10):
    Val=[]
    for j in range(0, i+1):
        z = Euclid_(Vecs[i], Vecs[j])
        Val.append(z)
    DisM.append(Val)
    
print("\n") 
print("Triangular Dissimilarity Matrix: \n")   
for dis in DisM:
    for i in range(len(dis)):
        print("%.6f" %dis[i], end=" ")
        
        
    print("\n")
"""
