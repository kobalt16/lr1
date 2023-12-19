import pandas as pd
from sklearn.linear_model import LinearRegression

df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('test.csv')


df1.head(15)

X_train = df1[['x']]
y_train = df1['y']
lr = LinearRegression()
lr.fit(X_train, y_train)

user_input = float(input('Введите число: '))

user_input_df = pd.DataFrame({'x': [user_input]})

prediction = lr.predict(user_input_df)

print('Предсказание:', x[0])