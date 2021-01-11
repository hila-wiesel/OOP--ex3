import matplotlib.pyplot as plt

if __name__ == "__main__":

    # shortest path:
    python_Time = [0.003044100000000105, 0.16587819999999986, 0.3664065000000001, 0.5725693000000001, 5.5938099,
                   23.3865353]
    java_Time = [0, 0.001, 0.125, 0.574, 1.139, 1.864]
    nx_Time = [0.000042600000000003746, 0.00031800000000004047, 0.004163300000000092, 0.004160300000000117,
               0.04573360000000015, 0.007643099999999237]
    name = ["Graph 1", "Graph 2", "Graph 3", "Graph 4", "Graph 5", "Graph 6"]
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(name, python_Time, linewidth=3.4, label="in python")
    plt.plot(name, java_Time, linewidth=3.4, label="in java")
    plt.plot(name, nx_Time, 'r--', linewidth=3.4, label="networkx")
    plt.title("Shortest Path", fontsize=20)
    ax1.set_ylabel("time (in seconds)", fontsize=13)
    ax1.legend()
    plt.figure(figsize=(10, 10))
    plt.savefig('Shortest_Path.png')

    # All Connected Component:
    python_Time = [0.0008001000000001923, 0.01461660000000009, 0.2632023000000001, 0.3570730000000002, 11.5917751,
                   112.7074927]
    java_Time = [0.0, 0.003, 0.084, 0.095, 1.973, 5.648]
    nx_Time = [0.00036520000000006547, 0.0010175999999999519, 0.00738430000000001, 0.025672999999999835,
               0.10816699999999813, 0.4398079999999993]
    ax2 = plt.subplot(1, 1, 1)
    plt.plot(name, python_Time, linewidth=3.4, label="in python")
    plt.plot(name, java_Time, linewidth=3.4, label="in java")
    plt.plot(name, nx_Time, 'r--', linewidth=3.4, label="networkx")
    plt.title("Connected Components", fontsize=20)
    ax2.set_ylabel("time (in seconds)", fontsize=13)
    ax2.legend()
    plt.savefig('SCCs.png')

    # Connected Component (for specific node):
    python_Time = [0.00046731999999110484, 0.0012980460000221682, 0.01693088299999772, 0.1279890199999977,
                   0.29987138100000155, 0.44094796800000213]
    java_Time = [2.2000000000000006E-4, 0.0010300000000000003, 0.007850000000000003, 0.0032700000000000016,
                 0.7273200000000002, 1.86068]
    ax3 = plt.subplot(1, 1, 1)
    plt.plot(name, python_Time, linewidth=3.4, label="in python")
    plt.plot(name, java_Time, linewidth=3.4, label="in java")
    plt.title("Connected Component (for id)", fontsize=20)
    ax3.set_ylabel("time (in seconds)", fontsize=13)
    ax3.legend()
    plt.figure(figsize=(10, 10))
    plt.savefig('SCC.png')
