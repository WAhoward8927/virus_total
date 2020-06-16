import os
import hashlib
from pathlib import Path


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


dup = {}
photo_path = 'G:/py_work'


def build_dup_dict(dir_path, pattern='*.xlsx'):
    def save(file):
        hash = md5sum(file)  # 儲存所有指定副檔名的MD5
        if hash not in dup.keys():
            dup[hash] = [file]
        else:
            dup[hash].append(file)
    p = Path(dir_path)
    for item in p.glob('**/' + pattern):
        save(str(item))


def main():
    def get_duplicate():
        return {k: v for k, v in dup.items() if len(v) > 1}
    build_dup_dict(photo_path)
    for hash, files in get_duplicate().items():
        print(files)


if __name__ == '__main__':
    main()
