import numpy as np
import matplotlib.pyplot as plt
import pwlf

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=float)
y = np.array([0, 12.05, 0, 12.66, 40.0, 
     0, 0, 0, 0, 5.1,
     0, 0, 3.51, 0, 0])

my_pwlf = pwlf.PiecewiseLinFit(x, y)
breaks = my_pwlf.fit(13)
print(breaks)

x_hat = np.linspace(x.min(), x.max(), 100)
y_hat = my_pwlf.predict(x_hat)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(x_hat, y_hat, '-')
plt.show()
