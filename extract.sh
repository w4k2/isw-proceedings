#!/bin/bash
rm -rf submissions/0*
python scripts/0_extract.py
python scripts/1_clean-up.py
# HERE HUMAN WORK
#python 2_build-documents.py
cp -r submissions/0* proceedings/papers/sources_pdftex/