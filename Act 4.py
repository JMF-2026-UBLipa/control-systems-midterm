import control as ctrl
import matplotlib.pyplot as plt


num = [1]          
den = [1, 2, 2]    


G = ctrl.tf(num, den)


print("Transfer Function:")
print(G)


poles = ctrl.poles(G)
zeros = ctrl.zeros(G)

print("\nPoles:", poles)
print("Zeros:", zeros)


ctrl.pzmap(G, grid=True)
plt.title("Pole-Zero Map")
plt.show()