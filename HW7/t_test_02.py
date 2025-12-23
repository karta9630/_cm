from scipy import stats

data=[58, 89, 100,77, 39]
data2 = [81, 64, 96, 58, 50]

t_stat, p_val = stats.ttest_ind(data, data2)  # 雙樣本 t 檢定
print(f"{stats.tmean(data):.2f}")
print(f"{stats.skew(data):.2f}\n")
print(f"{stats.tmean(data2):.2f}")
print(f"{stats.skew(data2):.2f}\n")
if stats.skew(data)==stats.skew(data2) :
    print("可合併")
else : print("False")