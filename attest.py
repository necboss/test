import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем one-hot кодировку
one_hot = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединяем исходный DataFrame и one-hot кодировку
data = pd.concat([data, one_hot], axis=1)

# Удаляем исходный столбец 'whoAmI', так как он больше не нужен
data.drop('whoAmI', axis=1, inplace=True)

data.head()