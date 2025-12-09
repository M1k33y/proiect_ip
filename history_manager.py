import time

history = []

def add_entry(cpu, ram, net_down, net_up):
    entry = {
        "time": time.strftime("%H:%M:%S"),
        "cpu": cpu,
        "ram": ram,
        "net_down": net_down,
        "net_up": net_up
    }
    history.append(entry)

def get_history():
    return history
