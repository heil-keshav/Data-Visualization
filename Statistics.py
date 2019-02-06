import math

# Variance
def var_(vals):
    avg = mean_(vals)
    dev=0
    for val in vals:
        dev += (val - avg) ** 2
    return dev / (len(vals)- 1)

# Standard Deviation
def std_(vals):
    return math.sqrt(var_(vals))
    
# Mean    
def mean_(vals):
    s=0
    for val in vals:
        s = s + int(val)
    return s/len(vals)
  
# Covariance  
# cov(x,y)=∑(xi−x¯)(yi−y¯) / (n-1)  
def Cov_(A, B):
    s=0
    avgA = mean_(A)
    avgB = mean_(B)
    for i in range(len(A)):
        s +=  (A[i]-avgA)*(B[i]-avgB)
    return s/(len(A)-1)

# Correlation
# Cor = Covxy / (stdx*stdy)
def Cor_(A, B):
    return Cov_(A, B)/(std_(A)*std_(B))        


# Calculating Scale factor and offset for every attribute
# Using Scale factor S = 1/(Pmax - Pmin)
# and Offset O = -Pmin/(Pmax-Pmin)
def calc_():
    S =[]
    O =[]
    #Fedu
    S.append(1/(4-0))
    O.append(0)
    
    #Mjob
    S.append(1/(4-0))
    O.append(0)
    
    #Reason
    S.append(1/(3-0))
    O.append(0)
    
    #Studytime
    S.append(1/(4-1))
    O.append(-1/(4-1))
    
    #Failures
    S.append(1/(3-0))
    O.append(0)
    
    #goout
    S.append(1/(5-1))
    O.append(-1/(5-1))
    
    #absences
    S.append(1/(93-0))
    O.append(0)
    
    #G1
    S.append(1/(20-0))
    O.append(0)
    
    #G2
    S.append(1/(20-0))
    O.append(0)
    
    #G3
    S.append(1/(20-0))
    O.append(0)
    
    return S, O
    
#    
def Vec_(S, O, rows):
    Vecs=[]
    for row in rows:
        Vals =[]
        for i in range(10):
            # Nominal Attributes i=1 & i=2 columns
            if i==1:
                x=0
                if row[i]=="teacher":
                    x=0
                elif row[i]=="health":
                    x=1
                elif row[i]=="services":
                    x=2
                elif row[i]=="at_home":
                    x=3
                else:
                    x=4
                Vals.append(S[i]*x + O[i])
            elif i==2:
                x=0
                if row[i]=="home":
                    x=0
                elif row[i]=="reputation":
                    x=1
                elif row[i]=="course":
                    x=2
                else:
                    x=3
                Vals.append(S[i]*x + O[i]) 
            else:
                Vals.append(S[i]*int(row[i]) + O[i])
        Vecs.append(Vals)
    return Vecs

def Hist_():



    
def Euclid_(A, B):
     sum_all=0
     for i in range(len(A)):
          # Nominal Attributes
          if i==1 or i==2:
              if A[i]!=B[i]:
                   sum_all += 1
          else:
              sum_all += (A[i]-B[i])*(A[i]-B[i])
     return math.sqrt(sum_all)/math.sqrt(len(A)) 
    
def Manhatt_(A, B):
     sum_all=0
     for i in range(len(A)):
          # Nominal Attributes
          if i==1 or i==2:
              if A[i]!=B[i]:
                   sum_all += 1
          else:
              sum_all += abs(A[i]-B[i])
     return (sum_all)/(len(A))  
    
 
            
            
