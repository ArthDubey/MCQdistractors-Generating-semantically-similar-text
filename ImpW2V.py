import numpy as np 
import string 
from nltk.corpus import stopwords 

def softmax(x): 
	"""Compute softmax values for each sets of scores in x."""
	e_x = np.exp(x - np.max(x)) 
	return e_x / e_x.sum() 

class word2vec(object): 
	def __init__(self): 
		self.N = 10
		self.X_train = [] 
		self.y_train = [] 
		self.window_size = 2
		self.alpha = 0.001
		self.words = [] 
		self.word_index = {} 

	def initialize(self,V,data): 
		self.V = V 
		self.W = np.random.uniform(-0.8, 0.8, (self.V, self.N)) 
		self.W1 = np.random.uniform(-0.8, 0.8, (self.N, self.V)) 
		
		self.words = data 
		for i in range(len(data)): 
			self.word_index[data[i]] = i 

	
	def feed_forward(self,X): 
		self.h = np.dot(self.W.T,X).reshape(self.N,1) 
		self.u = np.dot(self.W1.T,self.h) 
		#print(self.u) 
		self.y = softmax(self.u) 
		return self.y 
		
	def backpropagate(self,x,t): 
		e = self.y - np.asarray(t).reshape(self.V,1) 
		# e.shape is V x 1 
		dLdW1 = np.dot(self.h,e.T) 
		X = np.array(x).reshape(self.V,1) 
		dLdW = np.dot(X, np.dot(self.W1,e).T) 
		self.W1 = self.W1 - self.alpha*dLdW1 
		self.W = self.W - self.alpha*dLdW 
		
	def train(self,epochs): 
		for x in range(1,epochs):		 
			self.loss = 0
			for j in range(len(self.X_train)): 
				self.feed_forward(self.X_train[j]) 
				self.backpropagate(self.X_train[j],self.y_train[j]) 
				C = 0
				for m in range(self.V): 
					if(self.y_train[j][m]): 
						self.loss += -1*self.u[m][0] 
						C += 1
				self.loss += C*np.log(np.sum(np.exp(self.u))) 
			print("epoch ",x, " loss = ",self.loss) 
			self.alpha *= 1/( (1+self.alpha*x) ) 
			
	def predict(self,word,number_of_predictions): 
		if word in self.words: 
			index = self.word_index[word] 
			X = [0 for i in range(self.V)] 
			X[index] = 1
			prediction = self.feed_forward(X) 
			output = {} 
			for i in range(self.V): 
				output[prediction[i][0]] = i 
			
			top_context_words = [] 
			for k in sorted(output,reverse=True): 
				top_context_words.append(self.words[output[k]]) 
				if(len(top_context_words)>=number_of_predictions): 
					break
	
			return top_context_words 
		else: 
			print("Word not found in dicitonary") 


def preprocessing(corpus): 
	stop_words = set(stopwords.words('english'))	 
	training_data = [] 
	sentences = corpus.split(".") 
	for i in range(len(sentences)): 
		sentences[i] = sentences[i].strip() 
		sentence = sentences[i].split() 
		x = [word.strip(string.punctuation) for word in sentence 
									if word not in stop_words] 
		x = [word.lower() for word in x] 
		training_data.append(x) 
	return training_data 
	

def prepare_data_for_training(sentences,w2v): 
	data = {} 
	for sentence in sentences: 
		for word in sentence: 
			if word not in data: 
				data[word] = 1
			else: 
				data[word] += 1
	V = len(data) 
	data = sorted(list(data.keys())) 
	vocab = {} 
	for i in range(len(data)): 
		vocab[data[i]] = i 
	
	#for i in range(len(words)): 
	for sentence in sentences: 
		for i in range(len(sentence)): 
			center_word = [0 for x in range(V)] 
			center_word[vocab[sentence[i]]] = 1
			context = [0 for x in range(V)] 
			
			for j in range(i-w2v.window_size,i+w2v.window_size): 
				if i!=j and j>=0 and j<len(sentence): 
					context[vocab[sentence[j]]] += 1
			w2v.X_train.append(center_word) 
			w2v.y_train.append(context) 
	w2v.initialize(V,data) 

	return w2v.X_train,w2v.y_train 
    
corpus = open('Proc.txt')
epochs = 20
  
training_data = preprocessing(corpus) 
w2v = word2vec() 
  
prepare_data_for_training(training_data,w2v) 
w2v.train(epochs)  
  