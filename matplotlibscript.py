import matplotlib.pyplot as plt

'''
time = [0, 0.25, 0.5, 0.75]
plt.plot([0,0.5])
plt.plot(times, [0,0.5,1,1.2]), 'g--', time, [1, 2, 3, 4], 'r', label = "Some data")
plt.xlabel('Time (s)')
plt.legend()
plt.title("First plots")
'''

'''
#plt.plot(range(10))
fig, ax1 = plt.subplots()
time = [0, 1, 2, 3, 4, 5, 6]
co2 = [250, 265, 272, 260, 300, 320, 39]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#plt.plot(time, co2)
ax1.plot(time, co2, 'b--')
plt.xlabel('Time (decade)')
ax1.set_ylabel('CO2 concentration (ppm)')

ax2 = ax1.twinx()
ax2.plot(time, temp, 'y--')
ax2.set_ylabel('Temperature (degC)')

plt.show()

plt.savefig("myplot.pdf")
'''

