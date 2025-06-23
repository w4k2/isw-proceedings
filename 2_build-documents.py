# 1. walk around all directories
# 2. pdflatex --interaction=nonstopmode main.tex
# 3. bibtex main
# 4. pdflatex --interaction=nonstopmode main.tex
# najlepiej powtó©z dwa razy
# 5. copy to pdf's folder

import os

acmd = 'pdflatex --interaction=nonstopmode main.tex'
bcmd = 'bibtex main'

for i in range(30):
    if os.path.isdir('submissions/%04i' % i):
        print('THERE IS', i)
        os.system('cd submissions/%04i; %s; %s; %s; %s; %s' % (
            i,
            acmd, bcmd, acmd, bcmd, acmd
        ))