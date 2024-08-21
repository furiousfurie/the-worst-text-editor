import random
import string
def file_encryption(file_path):
          chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace
          cypher = ""
          chars = list(chars)
          keys = chars.copy()
          random.shuffle(keys)
          with open(file_path, "r") as file : content = file.read()
          with open(file_path, "w") as file :
              for letter in content :
                   index = chars.index(letter)
                   cypher += keys[index]
              file.write(cypher)

def file_decryption(file_path):
          chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace
          crypted_file = ""
          chars = list(chars)
          keys = chars.copy()
          random.shuffle(keys)
          with open(file_path, "r") as file : content = file.read()
          with open(file_path, "w") as file :
              for letter in content :
                   index = keys.index(letter)
                   crypted_file += chars[index]
              file.write(crypted_file)





     

