#!/usr/bin/env python
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
parser.add_argument('--format', type=str, choices = ['html','pdf'], default = 'html',required=False)
args = parser.parse_args()

# Assign arguments
qa_project = args.project
qa_flight = args.flight
qa_format = args.format
output_filename = qa_project+qa_flight

# Create environment vars to be used by the notebook
os.environ['QA_CL'] = 'command_line_mode'
os.environ['QA_PROJ'] = qa_project
os.environ['QA_FLIGHT'] = qa_flight

os.system('echo "export QA_QCL="command_line_mode"" >> ~/.qa_vars')
os.system('echo "export QA_PROJ="qa_project"" >> ~/.qa_vars')
os.system('echo "export QA_FLIGHT="qa_flight"" >> ~/.qa_vars')

# Execute the cells in the notebook
# Set PYDEVD_DISABLE_FILE_VALIDATION=1 to supress debugger warning about
# frozen modules causing debugger to miss breakpoints
os.system('PYDEVD_DISABLE_FILE_VALIDATION=1 jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=600 --execute --inplace QAtools_notebook.ipynb')

# Convert to HTML or PDF
if qa_format =='pdf':
    qa_format='webpdf'
os.system('jupyter nbconvert QAtools_notebook.ipynb --output '+output_filename+' --allow-chromium-download --no-input --to '+qa_format)
