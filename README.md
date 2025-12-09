==================================
PYTHON TASK MANAGER – OFFICIAL REQUIREMENT VERSION
Complete Beginner-Friendly Roadmap (Console + Optional UI)
==================================

1. OVERVIEW
-----------
This project is a simplified monitoring tool inspired by Windows Task Manager, 
htop, and btop. The goal is to create a program that displays computer resource 
usage, active processes, and allows basic management of those processes.

The program should run in the console (terminal), but may optionally include a 
simple graphical UI. It must show system statistics (CPU, RAM, SSD, battery, 
network), keep a usage history, allow custom configuration, and optionally export 
data as files.

This roadmap is adapted for first-year students, without advanced programming 
concepts. All explanations are simple and practical.

--------------------------------------------------------------

2. LEARNING GOALS
-----------------
Students will learn to:
- understand what CPU, RAM, SSD, battery, and network usage mean
- read system information using Python
- organize code into multiple modules
- build interactive console menus
- save and load history data
- optionally generate charts and export data
- optionally create a beginner-level UI

--------------------------------------------------------------

3. FUNCTIONAL REQUIREMENTS
--------------------------

FR1. Display system resource usage:
    - CPU usage (%)
    - RAM usage (%)
    - SSD usage or disk usage (%)
    - Battery level (%), charging status (only on laptops)
    - Network traffic (upload/download speed)

FR2. Display active processes:
    - PID
    - name
    - CPU% per process
    - memory usage per process

FR3. Show historical usage:
    - Save CPU/RAM/Network usage at each refresh
    - Allow user to view the history

FR4. Style settings:
    - Ability to change colors (light/dark or simple color schemes)
    - Ability to change refresh interval (e.g., 1s, 2s, 5s)

FR5. End/terminate processes:
    - User enters a PID
    - Program attempts to stop that process

FR6. Export features:
    - Export history to CSV
    - (Optional) Export to Excel or PDF
    - Export usage graphs as PNG (CPU/RAM/Network history)

FR7. Console menu:
    - Clear, simple options for viewing stats, processes, history, exports

FR8. Optional: Graphical UI with Tkinter
    - Displays resource usage in simple panels
    - Refresh button / automatic refresh
    - Plots CPU/RAM graphs inside the window (optional)

--------------------------------------------------------------

4. NON-FUNCTIONAL REQUIREMENTS
------------------------------

NFR1. The program should be simple, stable, and should not crash on invalid input.

NFR2. Use comments and descriptive variable names to help understanding.

NFR3. Use only basic Python and psutil + matplotlib (for graphs) if allowed.

NFR4. Code should be modular:
        - resource reading
        - process reading
        - history management
        - exporting
        - UI/console interface

NFR5. Must run on Windows; recommended to work on Linux/Mac too.

--------------------------------------------------------------

5. SUGGESTED FILE STRUCTURE
---------------------------

task_manager/
│
├── main.py                     # Entry point, console menu
│
├── resource_reader.py          # CPU, RAM, SSD, battery, network info
├── process_reader.py           # Process list and actions
├── history_manager.py          # Store & retrieve usage history
├── export_tools.py             # CSV, Excel, PDF, PNG exports
├── style_settings.py           # Color themes, refresh rate settings
│
├── ui_tkinter.py (optional)    # Simple graphical UI
│
└── utils.py                    # Helper functions

--------------------------------------------------------------

6. STEP-BY-STEP IMPLEMENTATION GUIDE
------------------------------------

STEP 1: Create the folder and files

STEP 2: Install psutil (if allowed)
    - psutil lets you read system resources easily:
        * psutil.cpu_percent()
        * psutil.virtual_memory()
        * psutil.disk_usage('/')
        * psutil.sensors_battery()
        * psutil.net_io_counters()
        * psutil.process_iter()

STEP 3: Implement resource_reader.py
    Functions to write:
        get_cpu_usage()
        get_ram_usage()
        get_disk_usage()
        get_battery_info()
        get_network_speeds()   # calculate upload/download differences over time

STEP 4: Implement process_reader.py
    Functions:
        get_process_list()
        end_process(pid)

STEP 5: Implement history_manager.py
    - Maintain a list that stores:
        timestamp, CPU, RAM, network
    - Save to a file (CSV)
    - Load history back

STEP 6: Implement export_tools.py
    - export_csv(history)
    - export_png(graph) using matplotlib

(Optional)
    - export_excel()
    - export_pdf()

STEP 7: Implement style_settings.py
    - store current theme (e.g., "light" or "dark")
    - store refresh interval (1s, 2s, 5s)
    - functions to update them

STEP 8: Build the console menu (main.py)
    Example menu:

    ===========================================
                PYTHON TASK MANAGER
    ===========================================
    1. View system resource usage
    2. View running processes
    3. Search process by name
    4. Change refresh interval
    5. Change color theme
    6. View usage history
    7. Export history (CSV/PNG)
    8. End a process
    9. Open graphical UI (optional)
    0. Exit

STEP 9: Add readable formatting and error handling

STEP 10: (Optional) Implement a simple UI in ui_tkinter.py
    - see section 8 for full explanation

--------------------------------------------------------------

7. HOW THE CONSOLE INTERFACE SHOULD LOOK
----------------------------------------

Example output:

CPU Usage:      34%
RAM Usage:      62%
Disk Usage:     55%
Battery:        87% (Charging)
Network:        120 KB/s down | 35 KB/s up

Example history view:

Time        CPU%    RAM%    Down KB/s    Up KB/s
-------------------------------------------------
12:01:05    31      60      100           28
12:01:06    33      61      120           32
12:01:07    34      62      110           35

--------------------------------------------------------------

8. OPTIONAL USER INTERFACE (UI)
-------------------------------

8.1. Why a UI?
    - Makes the project look more like real Task Manager or htop
    - Helps visualize usage with bars or small graphs
    - Good optional challenge

8.2. What UI library to use?
    - Tkinter (built into Python)
    - Very beginner-friendly
    - No installation required

8.3. What the UI should include?
    A. A window titled "Python Task Manager"
    B. Panels showing:
        - CPU usage bar
        - RAM usage bar
        - Disk usage
        - Battery info
        - Network usage
    C. A refresh button
    D. A process list displayed in a table form
    E. A history graph (optional, using matplotlib)
    F. A settings area: refresh rate, color scheme

8.4. How to structure ui_tkinter.py?
    - Create main window
    - Create frames for:
        * Resource bars
        * Process list
        * Buttons (Refresh, Export, Settings)
    - Update resource values on button press or on a timer
    - To show a graph, embed matplotlib in Tkinter (optional)

8.5. How refreshing works in the UI?
    - Every 1–5 seconds, depending on settings:
        call get_cpu_usage()
        update labels/bars
        refresh process list

--------------------------------------------------------------

9. FREQUENTLY ASKED QUESTIONS
-----------------------------

Q1: How do we get system information?
    Using psutil module. It talks directly to the operating system.

Q2: How do we get network speeds?
    By reading bytes_sent and bytes_recv twice, then calculating the difference.

Q3: How do we store history?
    Use a list of dictionaries and save it to CSV.

Q4: What if psutil is not allowed?
    Students can simulate values, but real monitoring is preferred.

Q5: How detailed should the UI be?
    The UI is OPTIONAL. Even a simple window with a refresh button is enough.

Q6: What exports are required?
    At minimum: CSV.
    PNG graph export is optional but recommended.

--------------------------------------------------------------

10. DELIVERABLES
----------------
Students must submit:
- Entire project folder
- A running console version (mandatory)
- Optional Tkinter UI
- Exported sample files (CSV, PNG)
- README describing how to run everything

==============================================================
END OF DOCUMENT
==============================================================

