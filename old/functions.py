def Quartile25(x):
    return x.quantile(0.25)
def Quartile75(x):
    return x.quantile(0.75)
def Interquartilerange(x):
    return x.quantile(0.75) - x.quantile(0.25)
#Functions to have a clean table (with caps)
def Mean(x):
    return x.mean()
def Median(x):
    return x.median()
def StDeviation(x):
    return x.std()