import control as ctrl
import matplotlib.pyplot as plt


def create_system():
    num = [1, 1, 2]
    den = [1, 2, 3, 1, 1]
    return ctrl.tf(num, den)


def analyze_system(G):
    print("\nTransfer Function G(s):")
    print(G)

    poles = ctrl.poles(G)
    zeros = ctrl.zeros(G)

    print("\nPoles of G(s):", poles)
    print("Zeros of G(s):", zeros)

    return poles, zeros


def plot_step_response(G):
    t, y = ctrl.step_response(G)

    plt.figure()
    plt.plot(t, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Output')
    plt.title('Step Response')
    plt.grid()
    plt.show()


def plot_pz_map(G):
    plt.figure()
    ctrl.pzmap(G, grid=True)
    plt.title("Pole-Zero Map of G(s)")
    plt.show()


def main():
    G = create_system()
    analyze_system(G)
    plot_step_response(G)
    plot_pz_map(G)


if __name__ == "__main__":
    main()