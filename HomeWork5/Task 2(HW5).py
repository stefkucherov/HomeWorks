def filt(a):
    if a > 0:
        return a


numbers = [23, 45, -67, 13, 28, -4]
a = filter(filt, numbers)
print(list(a))
