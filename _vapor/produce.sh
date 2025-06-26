#!/bin/bash
cd proceedings
pdflatex --interaction=nonstopmode main.tex
makeindex -s confproc2.ist main.idx
pdflatex --interaction=nonstopmode main.tex
pdflatex --interaction=nonstopmode main.tex