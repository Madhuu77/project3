import random
def Generate_otp(l):
    otp=''.join(random.choices('0123456789',k=l))
    return otp
otp=Generate_otp(4)
print(otp)
