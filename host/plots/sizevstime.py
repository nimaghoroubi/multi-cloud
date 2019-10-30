
import re
import os
import matplotlib.pyplot as plt
from pylab import *

benchmarks = {}
for filename in os.listdir(os.curdir + "/benchmarks"):

    regex = r'[0-9]+'
    nrWorkers = re.findall(regex, filename)[0]
    benchmarks[nrWorkers] = {}

    with open(os.curdir + "/benchmarks/" + filename) as file:
        nrRuns = None
        time = None
        for line in file:

            if "number_of_runs" in line:
                regex = r'[0-9]+'
                nrRuns = int(re.findall(regex, line)[0])

            if "total_time" in line:

                regex = r'[0-9]+\.[0-9]+'
                time = re.findall(regex, line)[0]

            if(nrRuns and time):
                benchmarks[nrWorkers][nrRuns] = float(time)
                nrRuns = None
                time = None


maximumRuns = 0
for benchmark in benchmarks:
    nrRuns = list(benchmarks[benchmark].keys())
    times = list(benchmarks[benchmark].values())
    if max(nrRuns) > maximumRuns:
        maximumRuns = max(nrRuns)

    print(benchmark)

    label = benchmark + " worker"
    if int(benchmark) > 1:
        label += "s"

    plt.plot(nrRuns, times, label=label)


plt.xticks(np.arange(0, max(nrRuns), 5))
plt.legend(loc='upper left')
plt.ylabel("Seconds")
plt.xlabel("Number of times")
plt.show()
# x = np.arange(27)
# time1 = time1 + [0] * 20
# plt.plot(x, time1)
# plt.plot(x, time8)

# plt.show()

w1 = 17.659420013427734
w4 = 6.39198112487793
w8 = 3.87300705909729
