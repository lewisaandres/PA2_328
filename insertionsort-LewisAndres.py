'''
name1: AJ1 Fahim1
name2: AJ2 Fahim2

assignment:PA2
'''
import sys
import random
import time
from tkinter.messagebox import QUESTION

class Solution:
	
	#This function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	#This function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count):
			output.append(i)
		return output

	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0,elements_count+1):
			output.append(random.randint(1,10))

		return output


	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if 	input_type == "b":
			output = self.function_b(elements_count)
		if 	input_type == "c":
			output = self.function_c(elements_count, seed)
		return output

	#Lewis Andres insertionSort algo. Used Professor Fahim's powerpoint notes for reference 
	def insertionSort(queryList: list, n: int) -> list:
		for i in range(n):
			key = queryList[i]
			j = i - 1
			
			while (j >= 0 and queryList[j] > key):
				queryList[j+1] = queryList[j]
				j = j - 1
			
			queryList[j+1] = key 
		return queryList

			
	def pa2_bubblesort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		
    	# your insertion sort algorithm comes here ...
		#LewisA's insertionSort algo function called here
		Solution.insertionSort(query_list, n) 

    	# end of insertion sort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]




if __name__ == '__main__':
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]
	
	obj = Solution()
	ret = obj.pa2_bubblesort(input_type, elements_count, seed)
	print(ret)

