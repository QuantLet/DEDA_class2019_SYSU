import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams


class IndexData():
	def __init__(self):
		#load data
		self.raw_data = pd.read_csv('indexprice.csv')	
	
	def minmax_scale_close_price(self,a,b):
		self.a = a
		self.b = b
		self.max_close = self.raw_data.close.max()
		self.min_close = self.raw_data.close.min()
		self.scaled_close = (self.b-self.a)*(self.raw_data.close-self.min_close)/(self.max_close-self.min_close)+self.a
		self.scaled_data = pd.DataFrame(np.transpose(np.array([self.raw_data.date.values,self.scaled_close.values])),columns=['date','scaled_price'])

	def select_train_period(self,start,end):
		self.train_start_index = self.scaled_data.date.where(self.scaled_data.date==start).dropna().index[0]
		self.train_end_index = self.scaled_data.date.where(self.scaled_data.date==end).dropna().index[0]+1
		
		
	def select_test_period(self,start,end):
		self.test_start_index = self.scaled_data.date.where(self.scaled_data.date==start).dropna().index[0]
		self.test_end_index = self.scaled_data.date.where(self.scaled_data.date==end).dropna().index[0]+1
		

	def assemble_data(self,seq_len):
		self.seq_len=seq_len
		#sequentialize both test and train set and store x and y values
		x_train_data = []
		y_train_data = []

		#Assemble Train Set
		for i in range(self.train_start_index,self.train_end_index-seq_len+1):
			
			x_train_data.append(self.scaled_data.scaled_price.iloc[i:i+seq_len])
			y_train_data.append(self.scaled_data.scaled_price.iloc[seq_len])

		self.x_train_data=np.array(x_train_data)
		self.y_train_data=np.array(y_train_data)
		#Assemble Test Set
		x_test_data = []
		y_test_data = []

		#Assemble Test Set
		for i in range(self.test_start_index,self.test_end_index-seq_len):
			
			x_test_data.append(self.scaled_data.scaled_price.iloc[i:i+seq_len])
			y_test_data.append(self.scaled_data.scaled_price.iloc[seq_len])

		self.x_test_data=np.array(x_test_data)
		self.y_test_data=np.array(y_test_data)


class LSTM_Model():
	def __init__(self,units):
		self.model = Sequential()
		self.model.add(LSTM(units=units, return_sequences=True, input_shape=(idx.seq_len,1)))
		self.model.add(LSTM(units=units))
		self.model.add(Dense(1))
		self.model.compile(loss='mean_squared_error', optimizer='adam')

	def fit(self,x_data,y_data,epochs,batch_size):
		self.model.fit(x_data.reshape((-1,idx.seq_len,1)), y_data, epochs=epochs, batch_size=batch_size, verbose=2)

	def predict(self,x_data):
		self.preds_scaled = self.model.predict(x_data.reshape((-1,idx.seq_len,1)))

	def calc_rmse(self):
		#therefore rescale
		self.preds = (self.preds_scaled-idx.a)*(idx.max_close-idx.min_close)/(idx.b-idx.a)+idx.min_close
		self.rmse = np.sqrt(np.mean(np.power(self.preds-idx.y_test_data,2)))

	def plot_results(self):
		ts = pd.DataFrame(idx.raw_data.close).set_index(idx.raw_data.date)
		train = pd.DataFrame(idx.raw_data.close.iloc[idx.train_start_index:idx.train_end_index]).set_index(idx.raw_data.date.iloc[idx.train_start_index:idx.train_end_index])
		test = pd.DataFrame(idx.raw_data.close.iloc[idx.test_start_index:idx.test_end_index]).set_index(idx.raw_data.date.iloc[idx.test_start_index:idx.test_end_index])
		preds = pd.DataFrame(self.preds).set_index(idx.raw_data.date.iloc[idx.test_start_index+idx.seq_len:idx.test_end_index])
		

		plt.plot(ts,label='omitted')
		plt.plot(train,label='train')
		plt.plot(test,label='test')
		plt.plot(preds,label='pred')
		plt.legend(loc='lower left')
		
		plt.xticks(ts.index[np.arange(1,ts.shape[0],50)],rotation=45)
		plt.show()



# Load and Prepare the data for the LSTM 	
idx=IndexData()
idx.minmax_scale_close_price(0,1)

idx.select_train_period(start='2017-01-03',end='2017-11-30')
idx.select_test_period(start='2017-11-30',end='2018-11-20')
idx.assemble_data(seq_len=60)

# Feed data to LSTM, train, predict test sample

lstm = LSTM_Model(units=50)
lstm.fit(x_data=idx.x_train_data,y_data=idx.y_train_data,epochs=1,batch_size=20)
lstm.predict(x_data=idx.x_test_data)
lstm.calc_rmse()
lstm.plot_results()





