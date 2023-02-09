from progress.bar import Bar
import time
import random

title = "Процесс    |Уровень загрузки                | Шаг загрузки и время выполнения"
print('-'*len(title))
print(title)
print('-'*len(title))
bar = Bar('Processing', max=20)
for i in range(20):
    a = random.random()
    time.sleep(a)
    bar.next()
    print(f'   {a}')
bar.finish()
print('-'*len(title))
print("Готово")
print('-'*len(title))
print()