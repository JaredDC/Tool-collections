import os
import hashlib

class Renamer:
    def __init__(self, path):
        self._path = path
        

    @staticmethod
    def mkdir(path):
        if os.path.exists(path):
            # print("path exists: %s" % path)
            pass
        else:
            os.makedirs(path)
            print("mkdir path: %s" % path)
    def get_hash_from_file(self, file_path="sample.txt"):
        hash_obj = hashlib.md5()
        block_size = 128 * hash_obj.block_size
        with open(file_path, 'rb') as f:
            chunk = f.read(block_size)
            while chunk:
                hash_obj.update(chunk)
                chunk = f.read(block_size)
            hash = hash_obj.hexdigest()
            return hash

    def run(self):
        folder = os.listdir(self._path)
        one = None
        i = 1
        for f in folder:
            if os.path.basename(f).endswith("jpg"):
                if os.path.basename(f)[0].isdecimal():
                    hash = self.get_hash_from_file(f)
                    suffix = os.path.basename(f).split(".")[1]
                    new_name = "h-" + hash + "." + suffix
                    print("{:0>2d}. [ {:^18s} ]   ->   [ {} ]".format(i, f, new_name))
                    i +=1
                    os.rename(f, new_name)
        print("RENAME ENDED.")   

    @staticmethod
    def opendir(path):
        path = path.replace('/', '\\')
        os.system("explorer.exe \"%s\"" % path)


def main(path):
    renamer = Renamer(path)
    renamer.run()
        

if __name__ == '__main__':
    path = u"D:\\jared\\erotic\\mr skin\\rename"
    main(path)