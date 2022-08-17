test = '120'
print(test)
res = bytearray(test, encoding='utf-8')
res1 = repr(test.encode('hex'))
print(res1)