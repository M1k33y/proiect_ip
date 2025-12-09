import psutil
import time

_previous_net = psutil.net_io_counters()
_previous_time = time.time()

def get_cpu_usage():
    return psutil.cpu_percent(interval=0.1)

def get_ram_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_battery_info():
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return {"percent": None, "plugged": None}
        return {"percent": battery.percent, "plugged": battery.power_plugged}
    except:
        return {"percent": None, "plugged": None}

def get_network_speeds():
    global _previous_net, _previous_time
    current_net = psutil.net_io_counters()
    current_time = time.time()

    delta_time = current_time - _previous_time
    download_speed = (current_net.bytes_recv - _previous_net.bytes_recv) / delta_time
    upload_speed = (current_net.bytes_sent - _previous_net.bytes_sent) / delta_time

    _previous_net = current_net
    _previous_time = current_time

    return download_speed, upload_speed
