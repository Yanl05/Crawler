

import os
import re

def rename(pathx):
    if os.path.isdir(pathx):
        path = pathx
        filelist = os.listdir(path)
        for files in filelist:
            print(files + '  1')
            p = re.compile(r'\[www.17zixueba.com\]')

            olddir = os.path.join(path, files)
            print(olddir+ '  2')
            newdir = p.sub("", olddir)
            print(newdir+'  3')
            os.rename(olddir, newdir)

            #path = pathx + '\\' + files
            t = path + '\\' + files
            if os.path.isdir(t):
                print(path + '\\' + files +  '  4')
                rename(path + '\\' + files)



rename('E:\\研究生自学视频')

