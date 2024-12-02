#!/usr/bin/env python

import os
import music21
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title(".mxl Measure Counter")
        
        # Folder path label and textbox
        tk.Label(self.master, text="Folder path:").grid(row=0, column=0, sticky="W")
        self.folder_path = tk.StringVar()
        tk.Entry(self.master, textvariable=self.folder_path, width=50).grid(row=1, column=0, padx=10, pady=5)
        
        # Browse button
        tk.Button(self.master, text="Browse...", command=self.browse_folder).grid(row=1, column=1, padx=10, pady=5)
        
        # Process button
        tk.Button(self.master, text="Process", command=self.process_files).grid(row=2, column=0, padx=10, pady=5)
        
        # Reset button
        tk.Button(self.master, text="Reset", command=self.reset).grid(row=2, column=1, padx=10, pady=5)
        
        # Status label
        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=3, column=0, padx=10, pady=5)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", maximum=100)
        self.progress_bar.grid(row=4, column=0, padx=10, pady=5)
        self.progress_var = tk.DoubleVar()
        
        # Processed files counter
        self.processed_files_label = tk.Label(self.master, text="")
        self.processed_files_label.grid(row=5, column=0, padx=10, pady=5)
        self.file_count = 0
        
        # Total measures counter
        self.total_measures_label = tk.Label(self.master, text="")
        self.total_measures_label.grid(row=6, column=0, padx=10, pady=5)
        self.total_measures = 0
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path.set(folder_path)

    def get_musicxml_files_count(self, folder_path):
        """
        Get the total number of MusicXML files (files with a .mxl extension) in the given folder and its subfolders.
        """
        musicxml_files_count = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith(".mxl"):
                    musicxml_files_count += 1

        return musicxml_files_count

    def process_files(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            self.status_label.config(text="Please enter a folder path.")
            return

        if not os.path.isdir(folder_path):
            self.status_label.config(text="Folder not found.")
            return

        self.status_label.config(text="Processing files...")
        self.master.update_idletasks()

        total_measures = 0
        file_count = 0
        musicxml_files_count = 0  # track MusicXML files only
        total_musicxml_files = self.get_musicxml_files_count(folder_path)

        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if not filename.lower().endswith(".mxl"):
                    continue

                if "(1)" in filename:
                    continue

                file_path = os.path.join(dirpath, filename)
                try:
                    score = music21.converter.parse(file_path)
                except music21.exceptions21.MusicXMLParseException:
                    continue

                measures = self.get_total_measures(score)
                total_measures += measures
                file_count += 1
                musicxml_files_count += 1  # increment MusicXML file count

                print(f"Processed file: {file_path}")

                # Update progress bar for MusicXML files only
                self.progress_var.set(musicxml_files_count / total_musicxml_files * 100)
                self.progress_bar['value'] = self.progress_var.get()
                self.master.update_idletasks()

        self.status_label.config(text=f"Processed {file_count} files.")
        self.processed_files_label.config(text=f"Total files processed: {file_count}")

        self.total_measures += total_measures
        self.total_measures_label.config(text=f"Total measures: {self.total_measures}")

    

    def get_total_measures(self, score):
        if not score.parts:  # If there are no parts, return 0
            return 0
        total_measures = 0
        # Only count measures in the first part
        first_part = score.parts[0]
        for measure in first_part.getElementsByClass('Measure'):
            total_measures += 1
        return total_measures

    def reset(self):
        self.status_label.config(text="")
        self.progress_var.set(0)
        self.progress_bar['value'] = self.progress_var.get()
        self.processed_files_label.config(text="")
        self.total_measures = 0
        self.total_measures_label.config(text="Total measures: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

