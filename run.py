import os

import tkinter as tk
import tkinter.filedialog as fd


root = tk.Tk()
root.withdraw()
selected_files = fd.askopenfilenames(parent=root, title='Choose a file')
for file in selected_files:
    print("Selected file: " + file)

ANIM_TO_VTK_PATH = "C:\\Users\\Work\\Desktop\\OpenRadioss\\exec\\anim_to_vtk_win64.exe"

for file in selected_files:
    command = ANIM_TO_VTK_PATH + " " + file + " > " + file + ".vtk"
    os.system(command)
    print('Created file: ' + file + ".vtk")
