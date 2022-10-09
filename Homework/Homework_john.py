import pandas as pd
import statistics

df = pd.DataFrame.from_dict({'Age':[pd.Interval(left = 1, right = 5, closed = "both"),
                                    pd.Interval(left = 6, right = 15, closed = "both"),
                                    pd.Interval(left = 16, right = 20, closed = "both"),
                                    pd.Interval(left = 21, right = 50, closed = "both"),
                                    pd.Interval(left = 51, right = 80, closed = "both"),
                                    pd.Interval(left = 81, right = 110, closed = "both")],
                             'Frequency':[200,450,300,1500,700,44]})
print(df)





# Total number of participants
n = df["Frequency"].sum()
print('Total number of participants:',n)

# Lower limit median
left = statistics.median_grouped(df["Age"]).left
print('Lower limit median:',left)

# Cumulative sum
cum_sum = sum(df["Frequency"][0:3])
print('The cumulative sum of the frequency:',cum_sum)

# Median of frequency
for a,interval in enumerate(df['Age']):
    if left <= interval.right:
        f = df['Frequency'][a]
        break
print('Median of the frequency:',f)


# Width of median class
width = df["Age"][3].length
print('The width is:', width)

median = (((n/2 - cum_sum)/f)*width) + left

print("The median is %.2f" % median)