# hello.py - http://www.graphviz.org/content/hello
import os

import cv2 as cv
from graphviz import Digraph

g = Digraph('G', filename='hello.gv')

g.attr('node', shape='record')

g.node('Hello', 'a|b|c|d|e')
g.edge('Hello', 'World')

filename = 'hello'
filepath = './run'
render_format = 'png'
#以png渲染生成文件
g.render(filename, filepath, view=False, cleanup=True, format=render_format);

img = cv.imread(filepath+'/'+filename+'.'+render_format)
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()

os.remove(filepath+'/'+filename+'.'+render_format);