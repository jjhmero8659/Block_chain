str = "RVJZJSRJVUFERUVJZXEGIZETZGCVBEFNERJRJLSJKZKLKZFEGVIDLKRKZFE\
EVKNFIBREUZJVWWZTZVEKZESFKYJFWKNRIVREUYRIUNRIV"
str_array = [];
letter_array = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
letter_count_array = []
max_value_index = []
max_value_letter = []
str_replace = "1"

def init():
    for i in range(0,len(str)):
        str_array.append(str[i])
    
    for i in letter_array:
        letter_count_array.append(0)

def check():
    for i in range(0,len(str)):
        for z in range(0,len(letter_array)):
            if(str[i] == letter_array[z]):
                letter_count_array[z] += 1

    max_value = max(letter_count_array)

    for i in range (0,5):
        max_value = max(letter_count_array)
        max_value_index.append(letter_count_array.index(max_value))
        letter_count_array[letter_count_array.index(max_value)] = 0;
        max_value_letter.append(letter_array[max_value_index[i]])

def translate(str_replace):
    for i in range(0,len(str_array)):
        for z in range(0,len(max_value_letter)):
            if(str_array[i] == max_value_letter[z]):
                str_array[i] = "E"
        str_replace = str_replace + str_array[i]
                
##    str_replace = "".join(str_array)
##    print(str_replace)

        
        

    

init();
check();
translate(str_replace)


print(str_array)
print(max_value_letter)
print(str_replace)


        
    
    
