import time
t0 = time.time()
print(t0)
time.sleep(1)
name = 'processing'

# 以 f开头表示在字符串内支持大括号内的python 表达式
print(f'{name} done in {time.time()} {time.time() - t0:.2f} s')
