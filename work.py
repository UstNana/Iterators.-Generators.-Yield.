import wikipedia
import json

class WriteFile:
  def __init__(self,n):
    self.file_w = open("as1.txt", "w", encoding="utf8")
    self.file_r = open("as.json", encoding="utf8")
    self.n = n

  def __iter__(self):
    return self

  def __next__(self):
    data_json = json.loads(self.file_r.read())
    for i in range(0,n):
      country = data_json[i]["name"]["common"]
      url = wikipedia.page(country).url
      self.file_w.write(country)
      self.file_w.write("-")
      self.file_w.write(url)
      self.file_w.write('\n')
      self.n +=1
      return url


if __name__ =="__main__":
  for item in WriteFile(10):
    print(item)
