import pandas as pd

l1 = [1,2,3,4]
#print(pd.Series(l1)) # Series is nothing but multi dimensional arry.
#print(pd.Series(l1,index=["One","Two","Three","Four"]))
data = pd.Series(l1,index=["One","Two","Three","Four"])
#print(data.index)
#print(data["One"])  # accessing the Index
#print(data[["One","Three"]])
#print(data[data>1])  # Manipulating with Index
d1 = {
      'EmpID':1,
      'EmpName':'Priya'
     }

emp1 = pd.Series(d1)
#print(emp1)

d2 = {
      'EmpID':2,
      'EmpName':'Shruthi'
     }

emp2 = pd.Series(d2)
#print(emp2)

employees = emp1 + emp2  #  Adding the series .., all the keys will be clubbed..
#print(employees)
#print(dir(employees))
employees = employees.T
#print(employees)


BusinessData = {
      'BusinessID': [11,22,33,44],
      'BusinessName':['Apple','Google','Facebook','Wtsapp'],
       'Starts': [4,6,8,2]
     }

bd = pd.DataFrame(BusinessData,index = ['One','Two','Three','Four'])
#print(bd.Starts) # accessing the data using columnname
#print(bd.T) # Transpose a Data Frame
bd= bd.T
#print(bd['One']) # Accesssing using coolumn name after transform
# print(bd.values) --> List of values
#pd.read_csv(index_col=[''],na_values=['NULL'])

df = pd.DataFrame([1,2,3,4])
print(df)
numerictoalpha = { 1:'one',
        2:'two',
        3:'three',
        4:'Four'
      }
#df = df.applymap(lambda x:'%.2f' % x)
df = df.applymap(lambda x: numerictoalpha)
print(df)


























