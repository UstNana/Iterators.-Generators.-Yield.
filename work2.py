import hashlib
import os

def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    with open( os.path.join(filename) , "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            yield m.update( buf )
    return m.hexdigest()

if __name__ =="__main__":
  for item in generate_file_md5("as.json"):
    print(item)
