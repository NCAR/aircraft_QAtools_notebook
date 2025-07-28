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
import pdfkit
from playwright.sync_api import sync_playwright
# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('--project', type=str, required=True)
parser.add_argument('--flight', type=str, required=True)
parser.add_argument('--format', type=str, choices = ['html','pdf'], default = 'html',required=False)
parser.add_argument('--hist', action='store_true', default=False, help='Generate interactive histogram notebook')
#boolean flag that defaults to false
args = parser.parse_args()

# Assign arguments
qa_project = args.project
qa_flight = args.flight
qa_format = args.format
qa_hist = args.hist
output_filename = qa_project+qa_flight
hist_filename = output_filename +'_aerosol-cloud'

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
os.system('PYDEVD_DISABLE_FILE_VALIDATION=1 jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=-1 --execute --inplace QAtools_notebook.ipynb')

# Convert to HTML or PDF

os.system('jupyter nbconvert QAtools_notebook.ipynb --output '+output_filename+' --no-input --to html')
# os.system('jupyter nbconvert QAtools_notebook.ipynb --output '+output_filename+' --no-input --allow-chromium-download --to webpdf --PDFExporter.paginate=False --PDFExporter.custom_args="[\'--no-sandbox\', \'--disable-dev-shm-usage\', \'--disable-gpu\', \'--memory-pressure-off\', \'--max-old-space-size=8192\', \'--virtual-time-budget=600\', \'--timeout=600\']" --HTMLExporter.theme=light')
# Convert to PDF based on format
def html_to_pdf_playwright(html_file, pdf_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Load the HTML file
        page.goto(f'file://{os.path.abspath(html_file)}')
        
        # Wait for content to load
        page.wait_for_load_state('networkidle')
        # Generate PDF with options
        page.pdf(
            path=pdf_file,
            print_background=True,
            prefer_css_page_size=True
        )
        
        browser.close()

try:
    html_to_pdf_playwright(f'{output_filename}.html', f'{output_filename}.pdf')
    print(f"PDF created successfully: {output_filename}.pdf")
except Exception as e:
    print(f"Playwright PDF conversion failed: {e}")

# Convert to HTML or PDF
if qa_hist == True:
    os.system('PYDEVD_DISABLE_FILE_VALIDATION=1 jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=-1 --execute --inplace interactive_hist.ipynb')
    os.system('jupyter nbconvert interactive_hist.ipynb --output '+hist_filename+' --no-input --to html')
#os.system('jupyter nbconvert --clear-output --inplace interactive_hist.ipynb')
#os.system('jupyter nbconvert interactive_hist.ipynb --output '+hist_filename+' --allow-chromium-download --no-input --to webpdf') ##Too large to run currently