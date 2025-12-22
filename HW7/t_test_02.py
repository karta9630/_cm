from scipy import stats

data=[58, 89, 100,77, 39]
data2 = [81, 64, 96, 58, 50]

t_stat, p_val = stats.ttest_ind(data, data2)  # 雙樣本 t 檢定
print(stats.tmean(data))
print(stats.skew(data))
print(stats.tmean(data2))
print(stats.skew(data2))
if stats.skew(data)==stats.skew(data2) :
    print("可合併")
else : print("False")