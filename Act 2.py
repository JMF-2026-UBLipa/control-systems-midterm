import control as ctrl
import matplotlib.pyplot as plt

num = [10, 20]
den = [1, 15, 50, 0]

G = ctrl.tf(num, den)

t, y = ctrl.step_response(G)

plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.grid()

# Save image
plt.savefig("step_response.png", dpi=300)

# Show plot
plt.show()