# Query-and-Document-Matching
## Approach
We have to match the ingredients with the article.i have got the description of every ingredients that include taste, veg/non veg, organic/inorganic, fruit or vegetable etc.,

The description is in the form of a CSV file which can be handled by pandas in python.

The article is broken into an array of words and splitting the whole document with spaces and special characters. The array is in the python program.

Every word in the description(CSV file) is checked with the article.

Finally every ingredient has its number of words matching. The ranking is done according to the maximum number of words matching.

The final ranking csv is saved in another csv file called out.csv
## Code execution
inp.csv is the input csv file of the description of the ingredients
article.txt is the text document of the article as input

run the run.py file 

out.csv is the output of the ranking of the ingredients
