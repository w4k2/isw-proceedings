import os
import glob

root = 'submissions/'

for path in glob.glob('*', root_dir=root):
    if os.path.isdir(root+path):
        # for all directories in root
        print('\nA', path)

        # purge some osx shit
        if '__MACOSX' in glob.glob('*', root_dir=root+path):
            os.system('rm -rf %s%s/__MACOSX' % (root, path))

        # check if some stupid lone directory and flatten it
        files = glob.glob('*', root_dir=root+path)
        if (len(files) == 1) & os.path.isdir(root+path+"/"+files[0]):
            pth_to_remove = root+path+"/"+files[0]
            pth_to_remove = pth_to_remove.replace(' ', '\ ')
            pth_to_remove = pth_to_remove.replace('(', '\(')
            pth_to_remove = pth_to_remove.replace(')', '\)')
            os.system('mv %s/* %s/' % (pth_to_remove, root+path))
            os.system('rm -rf %s' % pth_to_remove)

        # remove unnecessary

        for ext in ['pdf', 'gz', 'blg', 'bbl', 
                    'aux', 'log', 'txt', 'bst',
                    'cls']:
            os.system('rm -rf %s%s/*.%s' % (root, path, ext))

        # repair main.tex name
        texfile = glob.glob('*.tex', root_dir=root+path)[0]
        texfile = texfile.replace(' ', '\ ')
        os.system('mv %s%s/%s %s%s/main.tex' % (root,path,texfile,
                                                root,path))

        files = glob.glob('*', root_dir=root+path)
        print(files)
