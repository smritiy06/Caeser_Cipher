print('''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"    "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           ''')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            
            original_position = alphabet.index(letter)

            if encode_or_decode == "encode":
                shifted_position = original_position + shift_amount 
                shifted_position %= len(alphabet) #because 4%25 = 4 and 34 % 25=9 i.e 25+"9"
                output_text += alphabet[shifted_position]
            elif encode_or_decode == "decode":
                shifted_position = original_position - shift_amount 
                shifted_position %= len(alphabet) #because 4%25 = 4 and 34 % 25=9 i.e 25+"9"
                output_text += alphabet[shifted_position]
    print(f"Here's the {encode_or_decode}d result: {output_text}")



should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == "yes":
        caeser(text,shift,direction)
    else:
        should_continue = False
        print("Goodbye")
