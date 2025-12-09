import psutil

def get_process_list():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            processes.append({
                "pid": info['pid'],
                "name": info.get('name', 'Unknown'),
                "cpu": info.get('cpu_percent', 0.0),
                "memory": info.get('memory_percent', 0.0)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def end_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        return True
    except Exception as e:
        return False
