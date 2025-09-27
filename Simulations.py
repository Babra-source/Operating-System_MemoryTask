import tkinter as tk

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
canvas = tk.Canvas(GUI, width=800, height=600, bg="white")
canvas.pack(pady=20)

# Coordinates of the memory container
x1, y1, x2, y2 = 300, 100, 500, 500

# Draw the 3 sides (left, right, bottom) to make an open-top rectangle
canvas.create_line(x1, y1, x1, y2, fill="blue", width=3)   # left side
canvas.create_line(x2, y1, x2, y2, fill="blue", width=3)   # right side
canvas.create_line(x1, y2, x2, y2, fill="blue", width=3)   # bottom side

# --- Job List (at the left side) ---
jobs = [
    (1, 5760), (2, 4190), (3, 3290), (4, 2030), (5, 2550),
    (6, 6990), (7, 8940), (8, 740), (9, 3930), (10, 6890)
]

y_pos = 120   # starting y position for jobs
for job_id, size in jobs:
    # Draw each job as a rectangle
    canvas.create_rectangle(50, y_pos, 200, y_pos+25, fill="lightblue")
    canvas.create_text(125, y_pos+12, text=f"Job {job_id} ({size})")
    y_pos += 35  # space between jobs

GUI.mainloop()
