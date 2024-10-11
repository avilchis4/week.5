newphrase = "rainstorm"
            #012345678
            #123456789 -- college board verison
#create a new variable called shortphrase
#and assign it a value by slicing
#the new phrase variable by removing
#the first 3 characters
#and the last 3 characters
#first 3 characters are "rai"
#last 3 characters are "orm"
#substring (string, start, end)
shortphrase = newphrase[3:len(newphrase)-3]
print(shortphrase)
#explain len (newphrase)-3 = 9 - 3 = 6