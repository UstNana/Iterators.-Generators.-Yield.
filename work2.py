import hashlib
import os

def generate_file_md5(filename, blocksize=2**20):

    with open( os.path.join(filename) , "r" ) as f:
        while True:
            buf = f.readline(blocksize)
            s = buf.encode()
            m = hashlib.md5()
            if not buf:
                break
            m.update(s)
            yield m


if __name__ =="__main__":
  for item in generate_file_md5("as.json"):
    print(item)
