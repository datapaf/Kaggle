import pandas as pd

filename = './home-data-for-ml-course/train.csv'

train_data = pd.read_csv(filename)

# looking for SalePrice

y = train_data.SalePrice

for column in train_data.columns:
	if "oom" in column:
		print(column)