# MusicXML-Measure-Counter
Python script that leverages the music21 library and Tkinter to count the numbers of MusicXML files within a directory

# Measure Counting Tool with Python and Tkinter

The Measure Counting Tool is a Python script that uses the music21 library and Tkinter to analyze and count measures in MusicXML files. This tool provides an intuitive graphical user interface (GUI) for musicians, composers, and researchers to automatically process their music scores and extract essential information about measures.

## Getting Started

To use the Measure Counting Tool, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Measure-Counting-Tool.git
   ```

2. **Create a Virtual Environment:**
   ```bash
   cd Measure-Counting-Tool
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once the virtual environment is activated and the dependencies are installed, run the script:

```bash
python measure_counting_tool.py
```

The GUI application will open, allowing you to interact with the tool.

1. Enter the path to the folder containing your MusicXML files in the provided textbox or use the "Browse" button to select the folder.

2. Click the "Process" button to start the measure counting process. The tool will analyze each MusicXML file in the selected folder and display the progress using a progress bar.

3. Once the process is complete, the tool will display the total number of measures found in the files and the total number of files processed.

4. To reset the tool and start a new analysis, click the "Reset" button.

## Contributing

We welcome contributions to improve the Measure Counting Tool! To contribute, follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make the necessary changes and commit them:

   ```bash
   git add .
   git commit -m "Add your commit message here"
   ```

4. Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request to the main repository, explaining the changes you made.

## License

The Measure Counting Tool is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

## Acknowledgments

The Measure Counting Tool is inspired by the desire to automate music analysis and simplify the management of musical scores. We are grateful to the music21 library for its powerful music data analysis capabilities and Tkinter for providing an intuitive GUI platform. We also extend our thanks to all contributors who helped improve this tool. Your contributions are invaluable to the project's success.

Enjoy using the Measure Counting Tool! If you have any questions, feedback, or suggestions, feel free to reach out. Happy analyzing!
