Write a Python program that takes a Scrabble rack as a command-line argument and prints all "valid Scrabble English" words that can be constructed from that rack, along with their Scrabble scores, sorted by score. "valid Scrabble English" words are provided in the data source below. A Scrabble rack is made up of 2 to 7 characters.

Below are the requirements for the program:
- This needs to be able to be run as a command line tool as shown below (not an input statement!)
- Allow anywhere from 2-7 character tiles (letters A-Z) to be inputted. 
- Do not restrict the number of same tiles (e.g., a user is allowed to input ZZZZZQQ).
- Output the **total** list of valid Scrabble words that can be constructed from the rack as (score, word) tuples, sorted by the score and then by the word alphabetically as shown in the first example below.
- Then output 'Total number of words:' and the total number.
- You need to handle input errors from the user and suggest what that error might be caused by and how to fix it (i.e., a helpful error message)
- Implement wildcards as either `*` or `?`. There can be a total of **only** two wild cards in any user input (that is, one of each character: one `*` and one `?`). Only use the `*` and `?` as wildcard characters. A wildcard character can take any value A-Z. Replace the wildcard symbol with the letter in your answer (see the second example below). 
- Wildcard characters are scored as 0 points, just like in the real Scrabble game. A two wildcard word can be made, should be outputted and scored as 0 points.
- Allow a user to specify that a certain letter has to be at a certain location.

#### The Data
The file: http://courses.cms.caltech.edu/cs11/material/advjava/lab1/sowpods.zip contains all "valid Scrabble English" words in the official words list, one word per line.

An example invocation and output:
```
$ python scrabble.py "ZAEFIEE"

Examples for wildcard invocation and output:
```
$ python scrabble.py "?F"

$ python scrabble.py "PEN*?in"

Additional logic to enter Specific letter and its location can also be taken up be in order "letter location" eg: 'P' 0
```
$ python scrabble.py "PENguin" 'P' 0 'E' 1
