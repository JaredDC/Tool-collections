import os
import shutil
class RenameClip:
    def __init__(self, path, b_path):
        self._path = path
        self._b_path = b_path
    def move_path(self):
        l = os.listdir(self._path)
        move_list = list()
        for i in l:
            if i.endswith(".flv"):
                move_list.append(i)
                src_file = self._path + '\\' + i
                dest_file = self._b_path + '\\' + i
                if not os.path.exists(dest_file):
                    print("move to {}".format(dest_file))
                    shutil.move(src_file, self._b_path)
                else:
                    print("file exists:{}".format(dest_file))
        print("Move End.")
    def run(self):
        l = os.listdir(self._path)
        rename_list = list()
        for i in l:
            if i.endswith("_分段1.flv"):
                rename_list.append(i)
                prefix = i.split("_分段1.flv")[0]
                cliptwo = self._path + "\\" + prefix + "_分段2.flv"
                src_file = self._path + '\\' + i
                dest_file = self._path + '\\' + prefix + '.flv'
                if os.path.exists(cliptwo):
                    print("No need {} to {}".format(i, prefix + ".flv"))
                else:
                    print("Rename to {}".format(prefix + ".flv"))
                    if os.path.exists(src_file):
                        os.rename(src_file, dest_file)
        if not rename_list:
            print("Directory [{}] is clear.".format(self._path))
        print("Rename End.")


def rename(path, src, dest):
    src_file = path + '\\' + src
    dest_file = path + '\\' + dest
    try:
        if not os.path.exists(dest_file):
            print("move to {}".format(dest_file))
            shutil.move(src_file, dest_file)
        else:
            print("file exists:{}".format(dest_file))
    except Exception as e:
        print("{}".format(e))
    else:
        print("Rename End.")


def main():
    clip = RenameClip(path="D:\\jared\\Downloads", b_path="D:\\jared\\Videos\\bilibili")
    try:
        clip.run()
        clip.move_path()
    except Exception as e:
        print(e)
    finally:
        print("ALL END.")

# 使用B站下载助手,下载的视频需要改名+移动到相应的文件夹中.
if __name__ == '__main__':
    main()
    # rename('D:\\jared\\Videos', 'videoplayback.mp4', 'Family Trip to PoHang_Korea_MarchBlue Poolvila in PoHang.mp4')
