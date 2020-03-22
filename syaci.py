#Systemic Augumented Cognitive Intelligence(SyACI)
"""
Author : Anirudh Srivastav
Date: 12.08.2016 14:36:44

Description: An NLP based , generative hyperinteractive model,
requires minimal Data to train but requries multi user environment to
optiimise itself on virtual or real enviroments.

Tags: seq2seq, NLTK , Keras

"""
import numpy as np
import pandas as pd
from nltk import word_tokenize as tokenize
from urllib import request as req
import sys
import pyfolio as pf
# silence warnings
import warnings
import zipline



class syaci:

	sys.path.append('/Users/rammstein/Desktop/pyfolio/')
	warnings.filterwarnings('ignore')
	%load_ext zipline
	!zipline ingest
	%matplotlib inline
	"""docstring for syaci"""
	def __init__(self, arg):
		super(syaci, self).__init__()
		self.arg = arg
		setRules(self);

	def setRules(self):
		url = "http://www.gutenberg.org/files/2554/2554.txt"
		response = request.urlopen(url)
		raw = response.read().decode('utf8')
		type(raw)
		raw[:75]
	pass

#function to process random textand generate inference
	def pass_text(self, arg):
		sdata = pd.read_csv()
		for x in sdata(1,1000):
			pass
	pass
