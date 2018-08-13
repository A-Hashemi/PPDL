import numpy as np
import scipy as sp


class LWECiphertext(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __add__(self, other: LWE_Ciphertext):
        self.c1 = other.c1
        self.c2 = other.c2


class LWE(object):
    def __init__(self, l: int):
        self.__len = l

    @classmethod
    def __param_gen(cls) -> (int, int):
        p, q = 0, 0
        np.randint()
        return p, q

    def param_gen(self) -> None:
        pass

    def key_gen(self):
        pass

    def encrypt(self, m: bytearray) -> LWECiphertext:
        pass

    def decrypt(self, c: LWE_Ciphertext) -> bytearray:
        pass

    def __len__(self):
        return self.__len
