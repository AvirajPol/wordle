from random import choice

def choose_word():
    words = ["apple", "caped", "soupy", "dated", "sorts"]
    #return choice(words)
    return "apple"

def checkchoice(result, original_hashmap):
    val = input_value()
    
    if len(val) != 5:
        print("Please enter exactly a 5 letter word.")
        checkchoice(result, original_hashmap)
        return

    input_val = list(val)
    
    hashmap = original_hashmap.copy()
    
    arr1 = ["grey"] * 5
    
    for i in range(5):
        if input_val[i] == result[i]:
            arr1[i] = "green"
            hashmap[input_val[i]] -= 1
            

    for i in range(5):
        if arr1[i] != "green" and hashmap.get(input_val[i], 0) > 0:
            arr1[i] = "yellow"
            hashmap[input_val[i]] -= 1

    print("input val:", input_val)
    print(arr1)
    
    if input_val == result:
        print("correct guess")
    else:
        checkchoice(result, original_hashmap)

def input_value():
    val = input("Enter your 5 letter word: ")
    if val == "exit":
        exit()
    return val.lower()

def main():
    result = list(choose_word())
    hashmap = {}

    for char in result:
        hashmap[char] = hashmap.get(char, 0) + 1

    checkchoice(result, hashmap)

if __name__ == "__main__":
    main()