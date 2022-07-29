import pyDes
import base64

Key = "Gogenius"
Iv = "Gogen123"


# 加密
def encrypt_str(data):
    # 加密方法
    method = pyDes.des(Key, pyDes.CBC, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    # 执行加密码
    k = method.encrypt(data)
    # 转base64编码并返回
    return base64.b64encode(k)


# 解密
def decrypt_str(data):
    method = pyDes.des(Key, pyDes.CBC, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    # 对base64编码解码
    k = base64.b64decode(data)
    # 再执行Des解密并返回
    return method.decrypt(k)


Encrypt = encrypt_str("1234567")
print(Encrypt)
Decrypt = decrypt_str(Encrypt)
print(Decrypt)
