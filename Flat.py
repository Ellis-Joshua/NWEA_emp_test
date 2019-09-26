import argparse

def run_test(test_name, test_list, expected):
	# Run a test of the flatten method.
	print ()
	print(test_name + ":")
	print("Expected:")
	print(expected)
	output_list = flatten(test_list)
	print("Received:")
	print(output_list)
	assert output_list == expected, "Failure: " + test_name 
	print ("Pass")
	print("#############################################")

def test_suit():
	# Run a basic test suit of flatten.
	
	# Empty list test.
	run_test ("Empty list test", [] ,[])

	# Single integer test.
	run_test ("Single integer test", [1] ,[1])
	
	# Two elements test.
	run_test ("Two elements test", [1, 2] ,[1, 2])
	
	# Nested list test.	
	run_test ("Two elements test", [[1, 2]] ,[1, 2])

	# Mixed list test.
	run_test ("Two elements test", [1, [2, 3]] ,[1, 2, 3])

def flatten(in_list):
    # Take a nested list of integers and return a list of integers.
	
	out_list = []
	if isinstance(in_list, list):
		for item in in_list:
			item_list = flatten(item)
			for ints in item_list:
				out_list.append(ints)
	else:
		out_list.append(in_list)
	
	return out_list

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', nargs='+', help="The list of integers")
parser.add_argument('-t', '--test', type=bool, default=False, help="Wither or not your are running the test suit.")
args = parser.parse_args()
if args.test:
	test_suit()
else:
	print ("Input:")
	print(args.list)

	flat_list = flatten(args.list)
	print("Processed:")
	for cur in flat_list:
		print (cur)
	