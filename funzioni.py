import datetime
mese = datetime.datetime.now().month
anno = datetime.datetime.now().year

def somma(nums, s=0):
    for i in nums:
        s += i
    return s

def moltiplica(nums, p=1):
    for i in nums:
        p *= i
    return p

def media(nums):
    s = somma(nums)
    return s / len(nums)

def divisione(num1, num2):
    try:
        return num1 / num2
    except:
        return False

def modulo(num1, num2):
    try:
        return num1 % num2
    except:
        return False

def pari(num):
    if num % 2 == 0:
        return True
    return False

def bisestile(anno=anno):
    if anno % 4 == 0:
        return True
    else:
        return False

def giorni(mese=mese, anno=anno):
    if mese in [11,4,6,9]:
        return 30
    elif mese == 2:
        if bisestile(anno):
            return 29
        return 28
    else:
        return 31
    return False

