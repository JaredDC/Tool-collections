import os
from PIL import Image

# 返回当前工作目录
CURRENT_PATH = os.getcwd()

# 转换格式
IMG_EXP = ".png"

# 获取最高所有文件
cur_all_files = os.listdir(CURRENT_PATH)
# 转换列表
imgList = []


# 遍历文件夹，储存webp格式的路径到列表内
def findFileForImage(filePath):
    child_all_files = os.listdir(filePath)
    for child_file_name in child_all_files:
        sPath = os.path.join(filePath, child_file_name)
        if os.path.isdir(sPath):
            findFileForImage(sPath)
        n, e = os.path.splitext(child_file_name)
        if e.lower() == ".webp":
            imgList.append(os.path.join(filePath, n))


# 检索目录下所有的webp文件，如果是文件夹则继续向下检索
for file_name in cur_all_files:
    nPath = os.path.join(CURRENT_PATH, file_name)
    # 文件夹
    if os.path.isdir(nPath):
        findFileForImage(nPath)
        continue
    # 储存
    name, ext = os.path.splitext(file_name)
    if ext.lower() == ".webp":
        imgList.append(os.path.join(CURRENT_PATH, name))


# 转换图片
def convertImage():
    print("convertImage Start...")
    for webpPath in imgList:
        print(webpPath)

        # 打开图片并赋值一份新的图片
        img = Image.open(webpPath + ".webp")
        img.load()
        # 将赋值的图片修改后缀保存在原路径
        img.save(webpPath + IMG_EXP)
        # 删除原webp图
        os.remove(webpPath + ".webp")
    print("convertImage END.")

def png2ico():
    import os
    import PythonMagick	# 该模块需要下载whl进行安装
    #获取目录下文件名清单
    files = os.listdir()
    #对文件名清单里的每一个文件名进行处理
    for filename in files:
        portion = os.path.splitext(filename) # portion为名称和后缀分离后的列表
        if portion[1] ==".png": # 如果为JPG则更改名字
            newfile = portion[0]+".ico" # 要改的新后缀#改好的新名字
            # 进行格式转换
            img = PythonMagick.Image(filename)
            img.sample('256x256')
            path = os.path.join(newfile)	
            img.write(path)
            print("%s --> %s" % (filename, newfile))  

# ps: download PythonMagick (Unofficial Windows Binaries for Python Extension Packages) 
#  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonmagick
#     https://download.lfd.uci.edu/pythonlibs/q4trcu4l/PythonMagick-0.9.19-cp38-cp38-win32.whl
# ps: install PythonMagick (e.g. pip install PythonMagick-0.9.19-cp38-cp38-win32.whl)

# 执行
convertImage()
png2ico()