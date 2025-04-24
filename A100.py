# 100. Encrypt and decrypt a string using base64.
import base64
# s="I am Iorn-Man !!!!!"
# bytes_s=s.encode('ascii')
# print(bytes_s)
# base_string =base64.b64encode(bytes_s)
# print(base_string)
# base_string.decode('ascii')
# print(base_string.decode("ascii"))


s='I am iron man !!!'.encode('ascii')
encoded_s=base64.b64encode(s).decode("ascii")
print(encoded_s)

s1=encoded_s.encode('ascii')
decoded_s1=base64.b64decode(s1).decode("ascii")
print(decoded_s1)