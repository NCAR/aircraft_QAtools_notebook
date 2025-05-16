[![DOI:<10.26023>](http://img.shields.io/badge/DOI-10.26023-green.svg)](https://doi.org/10.26023/a0e3-4n78)

__Note: Information on the data flow is in this repos wiki__
## QAtools_notebook README

The QAtools_notebook is a Jupyter notebook that uses python to generate a set of interactive plots to aid NCAR RAF Science and Instrumentation Group in quick-detection of data quality status immediately following a flight. The notebook uses bokeh, metpy, and matplotlib to generate plots. The notebook requires that the flight netCDF is available via a defined path. You must update the path to point to the directory containing your data file(s).

### Installation

You will need git, conda, and firefox installed on the machine you are going to be running the notebook. 

Resource for installing / checking git and conda installation:

* https://github.com/git-guides/install-git
* https://conda.io/projects/conda/en/latest/user-guide/install/index.html

The notebook is stored in this GitHub repository. To clone the repository, execute the following on the command line:

`git clone https://github.com/NCAR/aircraft_QAtools_notebook`

If you do not wish to have a local git repository, you can simply download the .zip file from this repository:

https://github.com/NCAR/aircraft_QAtools_notebook

Then you will need to `cd` into the directory. There is a file `environment.yml` that contains a list of all of the dependencies needed to run the notebook. 

The following command can be used to create a conda environment based on the contents of the environment.yml file. 

`conda env create --file=environment.yml`

You will then need to activate this environment using this command:

`conda activate qatools`

If you wish to convert the output to a pdf using webPDF you will then need to install chromium using this command:

`playwright install chromium`

How to use this notebook:

### Option 1: Interactively

After installation is complete, you can either type `jupyter-lab` or `jupyter-notebook` depending on the interface you would prefer.

This will launch the notebook in your browser, and you can modify the code directly. The two variables that you will need to change for the given project and flight that you are interested in generating plots for are: `project` and `flight`. To run the code, click on a cell to select it, then press the play button in the toolbar above.

You can also update `interactive_histogram` to either True or False. Your selection will determine whether histogram / size distribution heatmap plots are generated for corresponding data. 

### Option 2: Command Line Mode

If you would like to generate HTML exports from the notebook automatically, you can execute the script `auto_export.py` which provides you with the ability to pass command line arguments for project and flight. These will be stored and passed into the notebook at execution time. Then once the plots are generated, the output will be exported to HTML without the code sections included. This is the approach that is used when processing data on the RAF Ground Station Computer, as this script `auto_export.py` is called by `push_data.py`. 

`./auto_export.py --project <PROJECT> --flight <FLIGHT>`

If you would like to generate a pdf export of the notebook using the same method, add the optional argument `--format pdf`:

`./auto_export.py --project <PROJECT> --flight <FLIGHT> --format pdf`

The repo is checked out at /home/local/aircraft_QAtools_notebook and if GDRIVE = True in fieldProc_setup, then then the output HTML will sync to Google Drive. Then it will sync to /scr/raf_Raw_Data/CAESAR/field_sync on EOL servers.

## CAUTION

Just because auto_export.py completes without error does not mean the HTML file contains valid plots. 

```
> ./auto_export.py --project ACCLIP --flight rf01
[NbConvertApp] Converting notebook QAtools_notebook.ipynb to notebook
[NbConvertApp] Writing 177795 bytes to QAtools_notebook.ipynb
[NbConvertApp] Converting notebook QAtools_notebook.ipynb to html
[NbConvertApp] Writing 425557 bytes to QAtools_notebook.html
```
Notice the small size of the QAtools_notebook.html file. It should be 200-400MB rather than 400KB. If you view the HTML file, the plots will show errors that need to be fixed.

