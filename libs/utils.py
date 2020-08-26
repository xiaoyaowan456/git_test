from hashlib import sha256
import os

def make_password(password):
    '''产生一个安全密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

    #计算哈希值
    hash_value = sha256(password)

    #产生随机盐, 长度32字节
    salt = os.urandom(16).hex()

    #加盐，产生安全密码
    safe_password = salt + hash_value

    return safe_password


def check_password(password,safe_password):
    '''检查密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

    #计算哈希值
    hash_value = sha256(password)

    # if hash_value == safe_password[32:]:
    #     return True
    # else:
    #     return False
#这种方法可以，也可以采用下一种方法：
#这种方法是直接把return的值是True 或者 False 直接返回回来了。
    return hash_value == safe_password[32:]