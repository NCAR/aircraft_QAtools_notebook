#! /Users/taylort/miniconda3/bin/python

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--project', type=str, required=True)
parser.add_argument('--flight', type=str, required=True)
args = parser.parse_args()

qa_project = args.project
qa_flight = args.flight
output_filename = qa_project+qa_flight+'.html'

os.environ['QA_CL'] = 'True'
os.environ['QA_PROJ'] = qa_project
os.environ['QA_FLIGHT'] = qa_flight

os.system('jupyter nbconvert --to notebook --execute QAtools_notebook.ipynb')
os.system('jupyter nbconvert QAtools_notebook.ipynb --no-input --to html')
os.system('mv QAtools_notebook.html ' + output_filename)

