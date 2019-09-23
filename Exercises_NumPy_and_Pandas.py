import numpy as np
import pandas as pd
from common import switch_case
from matplotlib import pyplot as plt

#Question 1 - 
# Numerical Analysis Exercises using NumPy – Rainfall Dataset


# import the monthly average values from `CorkRainfall.txt` as a numpy array
cork_rainfall = np.loadtxt(fname = "datasets/CorkRainfall.txt")

#(i) Print out the max ‘Most Rainfall in a Day’ value and the average ‘Most Rainfall in a Day’ value for the Cork data (that is, obtain the maximum value contained in this column of data and the average value in this column of data).

#print("avg_monthly_precip>>>",avg_monthly_precip)
print("[Year, Month, Total Rainfall, Most Rainfall in a Day, Number of Rain days]")

#max ‘Most Rainfall in a Day’ value 
max_most_rainfall = np.amax(cork_rainfall[:,3], axis=0)
print("Maximum Most Rainfall in a Day: ",max_most_rainfall)


#(ii) Display all unique years for which there is data in the dataset (you can use np.unique) Ask the user to select a specific year. You should then output the sum of the Rain Days column for that year (you do this by adding up the "Number of rain days” for all 12 rows pertaining to the selected year).

#average ‘Most Rainfall in a Day’ 
average_maxRainfall = np.mean(cork_rainfall[:,3], axis=0)
print("Average ‘Most Rainfall in a Day’: ",average_maxRainfall)

print("available years")
print(np.unique(cork_rainfall[:,0]).astype(int))

#selected_year = int(input("Enter the year: "))
selected_year = 1962
#output the sum of the Rain Days column for the year entered by user 
print(cork_rainfall[cork_rainfall[:, 0] == selected_year][:, 4].sum())

#(iii) Calculate the wettest month of the year in Cork based using the “Total Rainfall” value. The month that has the highest cumulative “Total Rainfall” value across all years should be classified as the wettest.

month_cum = np.empty(shape=[0])

for i in range(0,12):
    indices = np.arange(i,cork_rainfall.shape[0],12)
    #cumulative for each month across all the years and stored in month_cum
    month_cum = np.append(month_cum,[np.sum(np.take(cork_rainfall[:,2],indices))])
#fetch the index value of month with highest cumulative
result = np.where(month_cum == np.amax(month_cum))
index=0
print("Wettest month: ")
while index<len(result[0]):
    print(switch_case(int(result[index])+1))
    index+=1


#(iv) This question focuses on the Number of Rain days column. The user is asked to enter a maximum threshold value for the number of rain days. Your code should then output the percentage of the time (percentage of rows in the dataset) where the number of rain days is less than or equal to the threshold value. For example, if a user enters a maximum threshold value of 6, then your code should output the percentage of rows where the number of rain days fell below the threshold value of 6.

#max_threshold = int(input("Enter maximum threshold value: "))
max_threshold = 6

result_tuple = (np.where(cork_rainfall[:,4] <= max_threshold))
print("percentage of rows where the number of rain days fell below the threshold:")
print(len(result_tuple[0])/len(cork_rainfall[:,4])*100)

#(v) Calculate the average ‘total rainfall’ value for the summer months (June, July and August) and the Autumn months (Sept, Oct, Nov).

summer_indices = np.empty(shape=[0])
for i in range(5,8):
    indices = np.arange(i,cork_rainfall.shape[0],12)
    summer_indices = np.append(summer_indices,indices).astype(int)

total_rainfall_summer = np.sum(np.take(cork_rainfall[:,2],summer_indices))
avg_rainfall_summer = (total_rainfall_summer)/len(summer_indices)
print("avg rainfall summer:",avg_rainfall_summer)

autumn_indices = np.empty(shape=[0])
for i in range(8,11):
    indices = np.arange(i,cork_rainfall.shape[0],12)
    autumn_indices = np.append(autumn_indices,indices).astype(int)

total_rainfall_autumn = np.sum(np.take(cork_rainfall[:,2],autumn_indices))
avg_rainfall_autumn = (total_rainfall_autumn)/len(autumn_indices)
print("avg rainfall autumn:",avg_rainfall_autumn)

#(vi) Read in the contents of the file DublinRainfall.txt into a NumPy array. Append the all rows from the Dublin array to the Cork NumPy array. Calculate the average number of raindays for the new array and write the new NumPy array to a CSV file.

dublin_rainfall = np.loadtxt(fname ="datasets/DublinRainfall.txt")
np.savetxt("CorkDublinRainfall.csv", np.concatenate((cork_rainfall, dublin_rainfall)),['%d','%0.2d','%.1f','%.1f','%d'],delimiter=',', header='Year, Month, Total Rainfall, Most Rainfall in a Day, Number of Rain days',newline='\n')


#Question 2 - Numerical Analysis Exercises using NumPy Bike Dataset:

bike = np.loadtxt(fname = 'datasets/bike.csv', delimiter=',')

#(i) Calculate the average temperature value (column index 9) for the entire dataset. Note the temperature values in this column have been already normalized by dividing by 41.

print("average temperature value: ",np.sum(bike[:,9]*41)/len(bike[:,9]))

#(ii) Print out the average number of casual users for all days classified as holidays as well as the average for all days classified as non-holidays. (Note holidays =1 and non-holidays = 0). Holidays attribute is stored at index 5.

casual_usr_holiday = (bike[bike[:, 5] == 1][:, 13].shape[0])
avg_casual_usr_holiday = (bike[bike[:, 5] == 1][:, 13].sum())/casual_usr_holiday
print("avg casual usr for days as holiday: ", avg_casual_usr_holiday)

casual_usr_nonholiday = (bike[bike[:, 5] == 0][:, 13].shape[0])
avg_casual_usr_nonholiday = (bike[bike[:, 5] == 0][:, 13].sum())/casual_usr_nonholiday
print("avg casual usr for days as non-holiday: ",avg_casual_usr_nonholiday)

#(iii) Write NumPy code that will print out the total number of casual users for each month of the year. You would expect to see an increase in the number of casual users over the summer months and a decline for the winter months.

y = np.empty(shape=[0])
for i in range(1, 13):
    sum = bike[bike[:, 3] == i][:, 13].sum()
    print("month ",i,":",sum)
    y = np.append(y, sum)
x = np.arange(1,13)

plt.xlabel("months" "\n" "spring - summer - fall - winter") 
plt.ylabel("total number of casual users for each month") 

plt.plot(x,y) 
plt.show()

""" 
(iv)
We will now look at the relationship between temperature and the number of users (column index 15). Your code should work out the average number of users for the following temperature ranges.
• 1,6
• 6, 10
• 10, 15
• 15, 20
• 20, 25
• 25, 30
• 30, 35
• 35, 40
Remember the temperature values specified in the file have been normalised by dividing by 41. """

avg_per_range = np.empty(shape=[0])
temp_range = np.array([[1,6],[6,10],[10,15],[15,20],[20,25],[25,30],[30,35],[35,40]])
for i in range(0,len(temp_range)):
    for j in range(1):
        total_users = bike[(bike[:,9]*41>=temp_range[i,j])&(bike[:,9]*41<=temp_range[i,j+1])][:, 15].shape[0]
        avg_per_range = np.append(avg_per_range,bike[(bike[:,9]*41>=temp_range[i,j])&(bike[:,9]*41<=temp_range[i,j+1])][:, 15].sum()/total_users)
        #print(temp_range[i,j],",",temp_range[i,j+1],":",avg_per_range)
print(avg_per_range)

x = np.arange(1,9)

plt.xlabel("temperature range") 
plt.ylabel("average number of users") 

plt.plot(x,avg_per_range) 
plt.show()


"""
Question 3 - Numerical Analysis Exercises Pandas – Shark Attack Dataset:
 For each of the following questions you will use a dataset containing information on global shark attacks called attacks.csv.
Attribute Information:
The attributes recorded in the dataset are as follows:
0. Case Number
1. Date
2. Year
3. Type
4. Country
5. Area
6. Location
7. Activity
8. Name
9. Sex
10. Age
11. Injury
12. Fatal
13. Time
14. Species
15. Investigator or Source
You will notice in the dataset that some entries in the fatality column are recorded as UNKNOWN, n, F, etc. We ignore these entries and only consider entries that are uppercase ‘Y’ or ‘N’.
Open this file using Pandas read_csv() function. The data file is stored in a different encoding format so you can use the following line to read the data into a dataframe.
df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")

"""

df = pd.read_csv('datasets/attacks.csv', encoding = "ISO-8859-1")
# apply mask to dataframe, cleanup
df = df[(df['Fatal'] == 'Y')|(df['Fatal'] == 'N')]

#(i)
#What location globally has the highest number of shark attacks?


print("location with highest number of shark attacks: ", df["Location"].value_counts().idxmax())


#(ii)
#Read the shark attack dataset into a Pandas Dataframe.
#Determine the six countries that have experienced the highest number of shark attacks.

print(df["Country"].value_counts().head(6))

#(iii)
#Modify your code to print out the six countries that have experienced the highest number of fatal shark attacks.

df_fatal = df[df['Fatal'] == 'Y']
print(df_fatal["Country"].value_counts().head(6))

#(iv)
#Based on the data in the Activity column are you more likely to be attacked by a shark if you are “Surfing” or “Scuba Diving”.

df_activity = df[(df['Activity'] == 'Surfing')|(df['Activity'] == 'Scuba Diving')]
print("more likely to be attacked by following activity: ",df_activity["Activity"].value_counts().idxmax())

#(v)
#Determine from the dataset what percentage of all recorded shark attacks were fatal.
df_fatal = df[df['Fatal'] == 'Y']
print("percentage of fatal attacks: ",df_fatal['Fatal'].count()/df['Fatal'].count()*100)

#vi
#For each individual country, print out the percentage of fatal shark attacks (number of fatal shark attacks expressed as a percentage of the total number of shark attacks). Some countries have recorded 0 fatal and non-fatal attacks. Your code should only consider countries where the number of non-fatal and fatal attacks are greater than 0.
print(df_fatal["Country"].value_counts()/len(df_fatal)*100)