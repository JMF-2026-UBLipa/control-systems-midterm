import control as ctrl
import matplotlib.pyplot as plt

num = [1]               # Numerator
den = [1, 2, 2]         # Denominator s^2 + 2s + 2
G = ctrl.tf(num, den)
print(G)
<TransferFunction>: sys[0]
Inputs (1): ['u[0]']
Outputs (1): ['y[0]']

        1
  -------------
  s^2 + 2 s + 2
poles = ctrl.poles(G)
print("Poles:", poles)
Poles: [-1.+1.j -1.-1.j]
zero = ctrl.zeros(G)
print("Zero:", zero)
Zero: []
import matplotlib.pyplot as plt

ctrl.pzmap(G, grid=True)
plt.show()