import numpy as np
import matplotlib.pyplot as plt

jan = np.array([0, 0, 0, 0 , 0, 0, 0, 0, 0, 455, 1919, 1894, 1460, 1223, 1455, 1636, 1456, 373, 0, 0, 0, 0, 0, 0])
feb = np.array([0, 0, 0, 0, 0, 0, 0, 0, 139, 1962, 2820, 2698, 2176, 1716, 2073, 2506, 2559, 1931, 239, 0, 0 ,0, 0, 0])
mar = np.array([0, 0, 0, 0, 0, 0, 0, 170, 1822, 3172, 3556, 3477, 2772, 2177, 2773, 3430, 3474, 3287, 1859, 99, 0, 0, 0, 0])
apr = np.array([0, 0, 0, 0, 0, 0, 123, 1937, 3728, 4320, 4537, 4298, 3075, 2543, 3501, 4164, 4305, 4058, 3356, 1116, 7, 0, 0, 0])
may = np.array([0, 0, 0, 0, 0, 14, 931, 2956, 3717, 4231, 4452, 4141, 3044, 2704, 3578, 4207, 4320, 4069, 3524, 2186, 326, 0, 0, 0])
jun = np.array([0, 0, 0, 0, 0, 42, 1369, 2868, 3768, 4425, 4697, 4397, 3245, 2730, 3605, 4353, 4591, 4534, 4019, 2870, 931, 13, 0, 0])
jul = np.array([0, 0, 0, 0, 0, 18, 968, 3011, 3902, 4483, 4721, 4459, 3282, 2643, 3525, 4247, 4534, 4334, 4005, 2832, 829, 8, 0, 0])
aug = np.array([0, 0, 0, 0, 0, 0, 208, 2250, 3706, 4277, 4571, 4378, 3130, 2484, 3394, 4223, 4560, 4443, 3831, 1988, 129, 0, 0, 0])
sep = np.array([0, 0, 0, 0, 0, 0, 5, 875, 3151, 3826, 4112, 3800, 2689, 2300, 3226, 3773, 3906, 3613, 2171, 210, 0, 0, 0, 0])
okt = np.array([0, 0, 0, 0, 0, 0, 0, 60, 1483, 2899, 3143, 2754, 2037, 1898, 2602, 3094, 3021, 1996, 170, 0, 0, 0, 0, 0])
nov = np.array([0, 0, 0, 0, 0, 0, 0, 0, 128, 1386, 2024, 1823, 1441, 1414, 1792, 1891, 1498, 227, 0, 0, 0, 0, 0, 0])
dec = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 400, 1832, 1611, 1270, 1106, 1414, 1507, 1043, 25, 0, 0, 0, 0, 0, 0])


def calc_total_mwh_usage_day(day, max, number):
    summe = 0
    for i in range(24):
        summe += min(max*number, day[i])
    return summe


def sum_over_months_kWh(months, maxi, number):
    return calc_total_mwh_usage_day(months[0], maxi, number) * 31 + calc_total_mwh_usage_day(months[1], maxi, number) * 28 + calc_total_mwh_usage_day(months[2], maxi, number) * 31 + calc_total_mwh_usage_day(months[3], maxi, number) * 30 + calc_total_mwh_usage_day(months[4], maxi, number) * 31 + calc_total_mwh_usage_day(months[5], maxi, number) * 30 + calc_total_mwh_usage_day(months[6], maxi, number) * 31 + calc_total_mwh_usage_day(months[7], maxi, number) * 31 +calc_total_mwh_usage_day(months[8], maxi, number) * 30 + calc_total_mwh_usage_day(months[9], maxi, number) * 31 + calc_total_mwh_usage_day(months[10], maxi, number) * 30 +calc_total_mwh_usage_day(months[11], maxi, number) * 31


def range_over_numbers(months, maxi, start=1, ende=1501):#not including ende
    erg = np.zeros(ende-start)
    # ra = np.arange(start,ende)
    for i in range(start, ende):
        erg[i-start] = sum_over_months_kWh(months, maxi, i)
    return erg



font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

# Das sind die Variablen, die Ihr verändern könnt
years = 2.5
usd_per_kWh = 0.057
max_MW_miner = 0.0035
costs_per_MW = 150000
fixed_costs = 100000


fig, ax1 = plt.subplots()
start = 1
ende = 1501
y = range_over_numbers([jan, feb, mar, apr, may, jun, jul, aug, sep, okt, nov, dec], max_MW_miner*1000, start=start, ende=ende)
ax1.plot(np.arange(1, ende), years*y*usd_per_kWh, label=str(years)+" year mining revenue")
ax1.plot(np.arange(1,ende), np.arange(1,ende) * max_MW_miner * costs_per_MW + fixed_costs, label="approx. miner costs with " + str(int(costs_per_MW / 1000)) + "kUSD/MW")
ax1.plot(np.arange(1, ende), years * y * usd_per_kWh - np.arange(1,ende) * max_MW_miner * costs_per_MW - fixed_costs, label=str(years) + " year revenue - miner costs")
ax1.set_xlabel("number of miners", fontdict=font)
ax1.set_ylabel("USD", fontdict=font)
ax1.scatter(np.argmax(years * y * usd_per_kWh - np.arange(1,ende) * max_MW_miner * costs_per_MW - fixed_costs), np.max(years * y * usd_per_kWh - np.arange(1, ende) * max_MW_miner * costs_per_MW - fixed_costs), c="darkgreen")
ax1.annotate("(" + str(np.argmax(years * y * usd_per_kWh - np.arange(1,ende) * max_MW_miner * costs_per_MW - fixed_costs)) + "," + str(round(np.max(years * y * usd_per_kWh - np.arange(1, ende) * max_MW_miner * costs_per_MW - fixed_costs) / 1000)) + "kUSD)", (np.argmax(years * y * usd_per_kWh - np.arange(1, ende) * max_MW_miner * costs_per_MW - fixed_costs), np.max(years * y * usd_per_kWh - np.arange(1, ende) * max_MW_miner * costs_per_MW - fixed_costs)), c="darkgreen")
plt.grid()
plt.legend()
ax2 = ax1.twinx()
ax2.plot(np.arange(1,ende), 100 * (years * y * usd_per_kWh - np.arange(1,ende) * max_MW_miner * costs_per_MW - fixed_costs) / (np.arange(1, ende) * max_MW_miner * costs_per_MW + fixed_costs), label="prct. return", color="red")
ax2.set_ylabel("percentage", fontdict=font)
fig.tight_layout()
plt.legend()
plt.savefig("analysis_solar_mining.pdf", dpi=150)
plt.show()
