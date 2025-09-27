import tkinter as tk
from load_files import load_jobs, load_memory_blocks

GUI = tk.Tk()
GUI.title("GUI Allocation Systems")
GUI.geometry("1000x1000")

# Buttons frame at top
frame_buttons = tk.Frame(GUI)
frame_buttons.pack(side="top", pady=10)

# Add buttons inside the frame
Sim_best_fit = tk.Button(frame_buttons, text="Best Fit Allocation")
Sim_best_fit.pack(side="left", padx=10)

btn_down = tk.Button(frame_buttons, text="First Fit Allocation")
btn_down.pack(side="left", padx=10)

# Canvas below the buttons
canvas = tk.Canvas(GUI, width=1800, height=1600, bg="white")
canvas.pack(pady=20)

# Coordinates of the memory container
x1, y1, x2, y2 = 500, 200, 700, 700

memory = load_memory_blocks()
y_pos = 200
for block in memory:
    canvas.create_rectangle(500, y_pos, 650, y_pos+30, fill="yellow")
    canvas.create_text(700, y_pos+15, text=str(block))
    y_pos += 30


# Draw the 3 sides (left, right, bottom) to make an open-top rectangle
# canvas.create_line(x1, y1, x1, y2, fill="blue", width=3)   # left side
# canvas.create_line(x2, y1, x2, y2, fill="blue", width=3)   # right side
# canvas.create_line(x1, y2, x2, y2, fill="blue", width=3)   # bottom side


# --- Job List (at the left side) ---
jobs = load_jobs()

y_pos = 120   # starting y position for jobs
count = 0
for job_id, job_time, size in jobs:
    x1, y1, x2, y2 = 0, 0, 0, 0
    x1, y1, x2, y2 = 50, y_pos, 200, y_pos + 25
    # if count % 2 == 0:
    #     x1, y1, x2, y2 = 50, y_pos, 200, y_pos+25
    # elif count % 2 == 1:
    #     x1, y1, x2, y2 = 250, y_pos, 400, y_pos+25
    #     print(True)

    # Draw each job as a rectangle
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
    canvas.create_text(125, y_pos+12, text=f"Job {job_id} ({size})")
    y_pos += 35  # space between jobs
    # count += 1

GUI.mainloop()
