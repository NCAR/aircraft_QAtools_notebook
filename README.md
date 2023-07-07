EOL JupyterHub link: `https://eol-alma8a.eol.ucar.edu:8000/jupyter/`

DOI: 

Static HTML export URL:
`https://archive.eol.ucar.edu/raf/QAtools/TI3GERrf01.html`

# aircraft_QAtools_notebook

This notebook contains plots that match the format and type provided in the R based QAtools Shiny web application and corresponding project specific pdfs. This notebook can be run from the Earth Observing Laboratory's JupyterHub multi-user server at the URL above. Users will be prompted to enter their credentials in order to spawn an instance of the server. 

The only variables that the user must assign prior to executing the cells in the notebook are flight and project. Once these are assigned by modifying the code text in the cell, the user can select `Run` and then `Run All`. The plots will be generated in the notebook. 

Most of the plots are generated using a python package called Bokeh. Bokeh allows users to pan and zoom within each plot as well as export each plot to a png. 

If a user wants to modify the plots, they can do this inline and generate their changes. 

If a user wants to modify the plots for others to see, they must commit their change:
`git add QAtools_notebook.ipynb`
`git commit`
`git push`
