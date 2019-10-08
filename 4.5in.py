#PROGRAM TO FIND NUMBER OF MATCHED CHARACTERS IN TWO STRINGS
def nmatchedchar(str1,str2):
    assert str1.isalpha()
    assert str2.isalpha()

    temp1=str1.lower()
    temp2=str2.lower()

    count=0
    for ch1 in temp1:
        for ch2 in temp2:
            if ch1==ch2:
                count+=1
    return count
def main():
    firstname=raw_input("enter the first name:")
    lastname=raw_input("enter the last name:")
    print'no of character matched in',firstname,'and',lastname,':',nmatchedchar(firstname,lastname)
    
