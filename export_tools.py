import csv
import matplotlib.pyplot as plt

def export_csv(history, filename="history.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=history[0].keys())
        writer.writeheader()
        writer.writerows(history)
    return True

def export_graph_png(history, filename="usage_graph.png"):
    times = [h["time"] for h in history]
    cpu = [h["cpu"] for h in history]
    ram = [h["ram"] for h in history]

    plt.figure(figsize=(10,5))
    plt.plot(times, cpu, label="CPU %")
    plt.plot(times, ram, label="RAM %")
    plt.xlabel("Time")
    plt.ylabel("Usage %")
    plt.title("System Usage History")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return True
