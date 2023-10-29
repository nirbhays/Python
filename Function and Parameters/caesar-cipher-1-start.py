alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cipher_text = []
d_cipher_text=[]
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, idxshift):

    for i in plain_text:
        if i==" ":
            cipher_text.append(' ')
        else:
            index_of_letter=alphabet.index(i)
            j=index_of_letter+shift
            cipher_text.append(alphabet[j])
    print("".join(cipher_text))

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encripted_text,d_idxshift):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
      for letter in encripted_text:
        if letter==" ":
            d_cipher_text.append(' ')
        else:
            index_of_letter=alphabet.index(letter)
            new_position=index_of_letter-shift
            d_cipher_text.append(alphabet[new_position])
      print("".join(d_cipher_text))
if direction=="encode":
    encrypt(plain_text=text,idxshift=shift)
else:    
    decrypt(encripted_text=text, d_idxshift=shift)