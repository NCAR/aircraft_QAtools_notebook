[![DOI:<10.26023>](http://img.shields.io/badge/DOI-10.26023-green.svg)](https://doi.org/10.26023/a0e3-4n78)


# aircraft_QAtools_notebook

## Introduction
This notebook contains plots that match the format and type provided in the R based QAtools Shiny web application and corresponding project specific pdfs. The table of contents allows users to navigate to the section of interest. The majority of the plots are generated using a python package called `Bokeh`. `Bokeh` allows users to pan and zoom within each plot as well as export each plot to a png. The Skew-T plot uses a python package called `metpy`.

### Use Case 1: Jupyter Notebook on JupyterHub
The notebook can be run from the Earth Observing Laboratory's JupyterHub multi-user server, using a set of shared credentials or with CIT credentials. Users will be prompted to enter their credentials in order to spawn an instance of the server. 

The only variables that the user must assign prior to executing the cells in the notebook are flight and project. Once these are assigned by modifying the code text in the cell, the user can select `Run` and then `Run All`. The plots will be generated in the notebook. If a user wants to generate a set of interactive histogram / size distribution plots, they must set the flag `interactive_histogram==True`.

If a user wants to modify the plots, they can do this inline and generate their changes. If a user wants to modify the plots for others to see in separate checkouts, they must commit their change:

`git add QAtools_notebook.ipynb`

`git commit`

`git push`

#### Conda package management
Conda is used to control the packages required to run this notebook. The packages and versions are listed in the environment.yml file that is located at the top level of the repository. This file can be used to create a conda environment by executing the following command:

`conda env create -f environment.yml`
`conda activate <environment_name>`

#### Programmatic notebook execution
A notebook can be executed using this command from the command line:
`jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=600 --execute --inplace QAtools_notebook.ipynb`

### Use Case 2: HTML Exports
HTML exports for each flight are generated and are placed on EOL's web server. These files will render interactive plots in the same was as the Jupyter Notebook. They do not require any data file in order to render the interactive plots. In order to generate the HTML exports without the code shown, the following command is executed:
`jupyter nbconvert QAtools_notebook.ipynb --no-input --to html`

If you would like to pass arguments for project and flight from the command line, you can execute the included script auto_export.py which parses arguments for project (--project) and flight (--flight).

An example is:
`./auto_export QA_tools_notebook.ipynb --project <PROJECT> --flight <FLIGHT>`
