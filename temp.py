import matplotlib.pyplot as plt
num = [32.00, 32.0, 31.0, 31.0, 31.0, 32.0, 31.0, 30.0]
plt.figure(figsize=(16,9))
plt.xlabel('Reading')
plt.ylabel('Temperature')
plt.grid()
plt.ylim(0, 50)
plt.plot(range(len(num)), num)
plt.show()
