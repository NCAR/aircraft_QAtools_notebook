#! /bin/python3
#####################################################################
# Script to auto-generate QAtools Notebooks two arguments are 
# needed: Project and Flight the notebook is executed with the args
# passed into the notebook and then the notebook is exported 
# to html and renamed. The last step is to scp to /net/www
#
# Author: Taylor Thomas (2023)
#
# Copyright University Corporation for Atmospheric Research (2023
####################################################################

import argparse
import os

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('--project', type=str, required=True)
parser.add_argument('--flight', type=str, required=True)
args = parser.parse_args()

# Assign arguments
qa_project = args.project
qa_flight = args.flight
output_filename = qa_project+qa_flight+'.html'

# Create environment vars to be used by the notebook
os.environ['QA_CL'] = 'command_line_mode'
os.environ['QA_PROJ'] = qa_project
os.environ['QA_FLIGHT'] = qa_flight

os.system('echo "export QA_QCL="command_line_mode"" >> ~/.qa_vars')
os.system('echo "export QA_PROJ="qa_project"" >> ~/.qa_vars')
os.system('echo "export QA_FLIGHT="qa_flight"" >> ~/.qa_vars')

# Execute the cells in the notebook
os.system('jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=600 --execute --inplace QAtools_notebook.ipynb')

# Convert to HTML
os.system('jupyter nbconvert QAtools_notebook.ipynb --no-input --to html')

# Rename
os.system('mv QAtools_notebook.html ' + output_filename)

# Copy
try:
    os.system('scp ' + output_filename + ' ads@tikal.eol.ucar.edu:/net/www/raf/QAtools')
except:
    print('Error copying file ' + output_filename + ' to /net/wwww/raf/QAtools')
