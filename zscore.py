import pandas as pd 
import plotly.figure_factory as pf 
import plotly.graph_objects as pg 
import random 
import statistics as stats 
df  = pd.read_csv("School1.csv")
Marks = df["Math_score"].tolist()
finalList = []
def get1sampledata():
    sample = []
    for i in range(0,100):
        randtemp=random.randint(0,len(Marks)-1)
        sample.append(Marks[randtemp])
    meanofsample = stats.mean(sample)
    finalList.append(meanofsample)
for i in range(0,1000):
    get1sampledata()



popmean = stats.mean(Marks)
popstd = stats.stdev(Marks)
print("population mean  = ",popmean)
print("population standard deviation ",popstd)
samplemean = stats.mean(finalList)
samplestd = stats.stdev(finalList)
print("sample mean  = ",samplemean)
print("standard deviation of sample = ",samplestd)
## calculating the first,second and third standard deviantion 
fsstartingpoint = samplemean - samplestd
fsendingpoint = samplemean + samplestd
Ssstartingpoint = samplemean  - 2*samplestd
Ssendingpoint = samplemean + 2*samplestd
Tsstartingpoint = samplemean - 3*samplestd
Tsendingpoint = samplemean + 3*samplestd
## analyzing sample one 
school1sample = pd.read_csv("School_1_Sample.csv")
MathScore = school1sample['Math_score'].tolist()
scoremean = stats.mean(MathScore)
zscore = (scoremean-samplemean)/samplestd
print(zscore)