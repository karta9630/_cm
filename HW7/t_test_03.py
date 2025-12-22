from scipy import stats

data=[58, 89, 100,77, 39]
data2 = [81, 64, 96, 58, 50]
t_stat, p_val = stats.ttest_rel(data, data2)
print("t值:", t_stat)
print("p值:", p_val)