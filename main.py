import time
from resource_reader import *
from process_reader import *
from history_manager import *
from export_tools import *
from style_settings import *
from utils import format_speed


def show_system_info():
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()
    battery = get_battery_info()
    net_down, net_up = get_network_speeds()

    add_entry(cpu, ram, net_down, net_up)

    print("\n=== SYSTEM INFO ===")
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")
    print(f"Disk Usage: {disk}%")
    if battery["percent"] is not None:
        print(f"Battery: {battery['percent']}% ({'Charging' if battery['plugged'] else 'On Battery'})")
    print(f"Network Download: {format_speed(net_down)}")
    print(f"Network Upload:   {format_speed(net_up)}")

def show_processes():
    procs = get_process_list()
    print("\n=== PROCESSES ===")
    for p in procs[:20]:  # show first 20
        print(f"{p['pid']:6}  {p['name'][:20]:20}  CPU: {p['cpu']}%  RAM: {p['memory']:.2f}%")

def show_history():
    print("\n=== HISTORY ===")
    for h in get_history():
        print(h)

def menu():
    while True:
        print("\n==== PYTHON TASK MANAGER ====")
        print("1. View system info")
        print("2. View processes")
        print("3. End a process")
        print("4. View history")
        print("5. Export history to CSV")
        print("6. Export graph to PNG")
        print("7. Change refresh rate")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_system_info()
        elif choice == "2":
            show_processes()
        elif choice == "3":
            pid = int(input("PID to terminate: "))
            print("Success" if end_process(pid) else "Failed")
        elif choice == "4":
            show_history()
        elif choice == "5":
            export_csv(get_history())
            print("Exported CSV.")
        elif choice == "6":
            export_graph_png(get_history())
            print("Exported PNG graph.")
        elif choice == "7":
            sec = int(input("New refresh time (seconds): "))
            set_refresh_rate(sec)
        elif choice == "0":
            break

        time.sleep(get_settings()["refresh_rate"])

if __name__ == "__main__":
    menu()
