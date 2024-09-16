import os
import pandas as pd
import sys
from scipy.stats import kendalltau
from scipy.stats import spearmanr

subDirs = ["1993_1997",  "1998_2002", "2003_2007",  "2008_2012", "2013_2017",        "2018_2023",   "All_years_1993_2023"];
suffix = ["1993_1997",  "1998_2002", "2003_2007",  "2008_2012", "2013_2017",        "2018_2023",   "All"];
stump = "top_N_features_"
MI = "Mutual_Information_Score"
pearsons = "PersonsR"

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("MI vs MI, Kendall's tau")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+MI+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+MI+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(kendalltau(data1,data2,nan_policy="omit").statistic, end='')
    print()

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("MI vs Pearson's, Kendall's tau")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+MI+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+pearsons+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(kendalltau(data1,data2,nan_policy="omit").statistic, end='')
    print()

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("Pearson's vs Pearson's, Kendall's tau")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+pearsons+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+pearsons+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(kendalltau(data1,data2,nan_policy="omit").statistic, end='')
    print()

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("MI vs MI, Spearman's")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+MI+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+MI+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(spearmanr(data1,data2,nan_policy="omit").statistic, end='')
    print()

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("MI vs Pearson's, Spearman's")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+MI+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["MI_Score"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+pearsons+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(spearmanr(data1,data2,nan_policy="omit").statistic, end='')
    print()

for ind in range(7):
    print(" "+subDirs[ind], end='')
print()

print("Pearson's vs Pearson's, Spearman's")
for ind in range(7):
    fileName1 = subDirs[ind]+"/"+stump+pearsons+suffix[ind]+".csv"
    print(subDirs[ind], end='')
    df1 = pd.read_csv(fileName1)
    data1 = df1.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligned
    for ind2 in range(7):
        fileName2 = subDirs[ind2]+"/"+stump+pearsons+suffix[ind2]+".csv"
        df2 = pd.read_csv(fileName2)
        data2 = df2.sort_values(by=["Feature"])["correlation"].values #sort by attribute name to have the two series aligneds
        print(" ", end='')
        print(spearmanr(data1,data2,nan_policy="omit").statistic, end='')
    print()
