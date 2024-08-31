#Report#

The analysis was to parse a database for types of medical codexes present in the data

First part of the code is to import pandas to allow for easier importing of the .csv file
Imported the CSV file
I then printed the columns to identify codexes

Next part of code was to find and count the particular codexes present
     I ran into an early issue with the sample code given for this part,  The code as given was able to identify specific codexes, but not identify codex groups

     I instead opted to find all column values that started with a particular String like ICD and count those
     This worked well but created other issue later on with analysis
     I beleive my issue stems from 2 issues.
     1)Instead of creating a String  specific to ICD, I was creating a function that was finding all values that contained strings starting with ICD, and so many of the subsequent functions I needed to call were cumbersome or impossible to call on a function and would have been easier to implemenmt on a string or a list 
     2) I failed to recognize some of the values like DRG were not the beginning of the string but located somewhere within it.  This was giving me erroneous values later on

     I was able to parse the data and get results for some of the searches for null values but some were giving odd returns, which I realised were due to some of the codex anmes appearing in the miuddle of the string and not at the begginning

     If I had a little more time before the due date I'm pretty sure I could sort these issues out eventually.

Due to these issues, My data analysis is incomplete and innacurate

These sorts of issues are probably common when starting out with database management, but should be learned from and addressed when it comes to policy and implementation.  Simple aspects of a database like naming conventions can have a serious effect on how easy or not that data can be manipulated and worked with.  