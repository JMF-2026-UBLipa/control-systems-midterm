import control as ct
import matplotlib.pyplot as plt
import numpy as np

def analyze_system(num, den, title):
    sys = ct.TransferFunction(num, den)
    print(f"\n--- {title} ---")
    print(f"Transfer Function: {sys}")
    
    # Create subplots
    fig, (ax_step, ax_pz) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 2.1 Step Response
    t, y = ct.step_response(sys)
    ax_step.plot(t, y, lw=2, color='blue')
    ax_step.set_title(f'Step Response: {title}')
    ax_step.set_xlabel('Time (s)')
    ax_step.set_ylabel('Amplitude')
    ax_step.grid(True, linestyle='--')
    
    # 2.2 Pole-Zero Map
    poles = ct.poles(sys)
    zeros = ct.zeros(sys)
    ax_pz.scatter(np.real(poles), np.imag(poles), marker='x', s=100, color='red', label='Poles')
    if len(zeros) > 0:
        ax_pz.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, facecolors='none', edgecolors='green', label='Zeros')
    
    ax_pz.axhline(0, color='black', lw=1)
    ax_pz.axvline(0, color='black', lw=1)
    ax_pz.set_title(f'Pole-Zero Map: {title}')
    ax_pz.set_xlabel('Real')
    ax_pz.set_ylabel('Imaginary')
    ax_pz.legend()
    ax_pz.grid(True, linestyle='--')
    
    plt.tight_layout()
    plt.show()

# Problem 1: G(s) = (s + 1) / (s^4 + 4s^3 + 7s^2 + 6s + 3)
analyze_system([1, 1], [1, 4, 7, 6, 3], "Problem 1")

# Problem 2: G(s) = 1 / (s^4 + 2s^3 + 3s^2 + 2s)
analyze_system([1], [1, 2, 3, 2, 0], "Problem 2")

# Problem 3: G(s) = 6 / (16s^4 + 16s^3 + 48s^2 + 36s)
analyze_system([6], [16, 16, 48, 36, 0], "Problem 3")
