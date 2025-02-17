Install Python (Windows 11)
Download Python (latest stable version) from [Python](Python.org).
Install it and check "Add Python to PATH" during installation.
Verify installation
```
python --version
```
Install Anaconda (Recommended)
Anaconda is a Python distribution that includes useful libraries and Jupyter Notebook.
Download and install Anaconda.
Open Anaconda Prompt and verify installation:
```
conda --version
```
Install Key Python Libraries
After installation, open Anaconda Prompt (or Command Prompt) and type:
```
pip install numpy pandas matplotlib scipy geopandas rasterio jupyter
```

To test, launch Jupyter Notebook:
```
jupyter notebook
```
Create a new Python notebook and test:
```
print("Hello, Geologists!")
```
