#!/bin/bash
rm -rf submissions/0*
python 0_extract.py
python 1_clean-up.py
# HERE HUMAN WORK
python 2_build-documents.py