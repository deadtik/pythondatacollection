import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

parameters = []
skills = []

def add_parameter():
    param = simpledialog.askstring("Input", "Enter Parameter Name:")
    value = simpledialog.askfloat("Input", f"Enter Value for {param}:")
    grade = simpledialog.askstring("Input", f"Enter Grade for {param} (A/B/C/D):").upper()
    description = simpledialog.askstring("Input", f"Enter Description for {param}:")
    parameters.append({"Parameter": param, "Value": value, "Grade": grade, "Description": description})

def add_skill():
    skill = simpledialog.askstring("Input", "Enter Skill Name:")
    grade = simpledialog.askstring("Input", f"Enter Grade for {skill} (A/B/C/D):").upper()
    skills.append({"Skill": skill, "Grade": grade})

def visualize():
    # Plot skills data
    grades_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    skill_names = [s['Skill'] for s in skills]
    skill_scores = [grades_mapping[s['Grade']] for s in skills]
    
    plt.figure(figsize=(10, 6))
    plt.barh(skill_names, skill_scores, color="skyblue")
    plt.xlabel("Grade (A=4, B=3, C=2, D=1)")
    plt.title("Skill Assessment")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    # Save or show visualization
    save_as_pdf = messagebox.askyesno("Export", "Would you like to save the visualization as a PDF?")
    if save_as_pdf:
        pdf_filename = simpledialog.askstring("Save PDF", "Enter filename (e.g., 'output.pdf'):")
        with PdfPages(pdf_filename) as pdf:
            pdf.savefig()
        messagebox.showinfo("Success", f"Visualization saved as {pdf_filename}.")
    else:
        plt.show()

# GUI
root = tk.Tk()
root.title("Data Input")

tk.Button(root, text="Add Parameter", command=add_parameter).pack(pady=5)
tk.Button(root, text="Add Skill", command=add_skill).pack(pady=5)
tk.Button(root, text="Visualize", command=visualize).pack(pady=10)

root.mainloop()
