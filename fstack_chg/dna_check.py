#Main function to check for sequences of repeated dna code
#EMV
import os
import json
import logging
from dynapp import save_entry

def cerebro(event,context):
	#base validation
	data = json.loads(event['body'])
    if 'dna' not in data:
        logging.error("Validation Failed")
        raise Exception("Expected data in 'dna' key")
        return
	if(scan_dna(data['dna'])):
		response = {
        "statusCode": 200,
        "body": "Mutation found!"                  
    	}
    else:
    	response = {
        "statusCode": 403,
        "body": "No mutation found"                  
    	}
    return response


def scan_dna(dna)
	n = len(dna)
	mcount = 0
	gna = ['A','C','G','T']
	for element in gna:		
		#horizonal lookup
		for i in range(n-3):
			for j in range(n):
				if dna[j][i] == element and dna[j][i+1] == element and dna[j][i+2] == element and dna[j][i+3] == element:
					mcount += 1
					if(mcount>1):
						print('mutant!')
						return True
		#vertical lookup
		for i in range(n):
			for j in range(n-3):
				if dna[j][i] == element and dna[j+1][i] == element and dna[j+2][i] == element and dna[j+3][i] == element:
					mcount += 1
					if(mcount>1):
						print('mutant!')
						return True
		#positive diagonal lookup
		for i in range(n-3):
			for r in range(n-3):
				if dna[j][i] == element and dna[j+1][i+1] == element and dna[j+2][i+2] == element and dna[j+3][i+3] == element:
					mcount += 1
					if(mcount>1):
						print('mutant!')
						return True
		#negative diagonal lookup
		for i in range(n-3):
			for r in range(3, n):
				if dna[j][i] == element and dna[j-1][i+1] == element and dna[j-2][i+2] == element and dna[j-3][i+3] == element:
					mcount += 1
					if(mcount>1):
						print('mutant!')
						return True
	return False