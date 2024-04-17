import itertools

names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fiona', 'Grace', 'Heidi', 'Ivan', 'Judy']
ages = [24, 50, 18]

# itertools.cycleを使ってagesリストを無限に繰り返す
cycled_ages = itertools.cycle(ages)
print(cycled_ages)
# zipを使ってnamesとcycled_agesを組み合わせる
# zipの第二引数にはnamesの長さに合わせてイテレーションする
for name, age in zip(names, cycled_ages):
    print(name, age)
