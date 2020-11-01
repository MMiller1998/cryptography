plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
initial_perm_inverse = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
PC1_perm = [57, 49, 41, 33, 25, 17, 9, 
        1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 
        19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4 ] 

PC2_perm = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

expansion_perm = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

final_f_perm = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

sboxes =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],  
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],  
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],  
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],  
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],  
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],  
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],  
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],  
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],  
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],  
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],  
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],  
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],  
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],  
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],  
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],  
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],  
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],  
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],  
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],  
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],  
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],  
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],  
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],  
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],  
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],  
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],  
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],  
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],  
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],  
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

#returns decimal rep of our hex digit
def hex_to_decimal(hex_digit):
    if hex_digit == 'F':
        return 15
    elif hex_digit == 'E':
        return 14
    elif hex_digit == 'D':
        return 13
    elif hex_digit == 'C':
        return 12
    elif hex_digit == 'B':
        return 11
    elif hex_digit == 'A':
        return 10
    else:
        return ord(hex_digit) - 48

# converts a digit in decimal to an array representing the digit in binary.
# Only works for 4 bit binary
def decimal_to_binary(dec_digit):
    binary_num = [0] * 4

    power_of_two = 3
    while(dec_digit > 0):
        binary_num[power_of_two] = dec_digit % 2
        dec_digit = dec_digit // 2

        power_of_two -= 1

    return binary_num

# returns an array of 4 integers representing the input in binary
def hex_to_binary(hex_digit):
    return decimal_to_binary(hex_to_decimal(hex_digit))

def binary_to_decimal(binary_array):
    decimal_array = [None for i in range(16)]
    for i in range(16):
        num = binary_array[(4 * i):(4 * i + 4)]
        sum = 0
        power_of_two = 3
        for j in range(len(num)):
            sum += num[j] * (2**power_of_two)
            power_of_two -= 1
        decimal_array[i] = sum
    return decimal_array

def decimal_to_hex(decimal_array):
    hex_array = [None for i in range(len(decimal_array))]
    for i in range(len(decimal_array)):
        if decimal_array[i] == 15:
            hex_array[i] = 'F'
        elif decimal_array[i] == 14:
            hex_array[i] = 'E'
        elif decimal_array[i] == 13:
            hex_array[i] = 'D'
        elif decimal_array[i] == 12:
            hex_array[i] = 'C'
        elif decimal_array[i] == 11:
            hex_array[i] = 'B'
        elif decimal_array[i] == 10:
            hex_array[i] = 'A'
        else:
            hex_array[i] = str(decimal_array[i])

    return hex_array

# Convert an array of 0's and 1's to a string in hex
def binary_to_hex(binary_array):
    decimal_array = binary_to_decimal(binary_array)
    return decimal_to_hex(decimal_array)

# Turns the given key into a binary matrix as defined in the notes
def hex_key_to_key_matrix(key):
    binary_matrix = [[] for i in range(8)]
    i = 0
    j = 0
    for hex_digit in key:
        key_element = hex_to_binary(hex_digit)

        for binary_digit in key_element:
            binary_matrix[i].append(binary_digit)

        j += 1
        if(j % 2 == 0):
            i += 1

    return binary_matrix

# convert the constructed key matrix into a flat list
def flatten_key_matrix(key_matrix):
    key_array = []
    for line in key_matrix:
        key_array += line
    return key_array

# Permutes a key array according to the given permutation
def permute_key_array(key_array, permutation):
    permuted_key_array = [None for i in range(len(permutation))]
    for i, j in zip(range(len(permuted_key_array)), permutation):
        j -= 1 #Permutation matrices are indexed at 1, not 0, so we need to adjust
        permuted_key_array[i] = key_array[j]
    return permuted_key_array

def v(i):
    if(i == 1 or i == 2 or i == 9 or i == 16):
        return 1
    else:
        return 2

def PC1(key_array):
    permuted_key = permute_key_array(key_array, PC1_perm)

    c = permuted_key[:28]
    d = permuted_key[28:]
    return [c, d]

def PC2(C, D):
    B = C + D
    return permute_key_array(B, PC2_perm)

def left_shift(string, i):
    return string[i:] + string[:i]

def generate_round_keys(key):
    round_keys = [[] for i in range(16)]

    c, d = PC1(key)
    print("C_0 = ", "".join(map(str, c)), "D_0 = ", "".join(map(str, d)))
    for i in range(16):
        c = left_shift(c, v(i + 1))
        d = left_shift(d, v(i + 1))

        round_keys[i] = PC2(c, d)
        
        print("C_" + str(i + 1) + " =", "".join(map(str, c)), "D_" + str(i + 1) + " =", "".join(map(str, d)))
        print("K_" + str(i + 1) + " =", "".join(map(str, round_keys[i])))

    return round_keys

def hex_key_to_round_keys(hex_key):
    binary_key = flatten_key_matrix(hex_key_to_key_matrix(key))
    
    return generate_round_keys(binary_key)

def expand(RHS):
    return permute_key_array(RHS, expansion_perm)

def s_box(box_index, input):
    row = 2 * input[0] + input[5]
    column = 8 * input[1] + 4 * input[2] + 2 * input[3] + input[4]
    return decimal_to_binary(sboxes[box_index][row][column])
    

def f(RHS, key):
    new_RHS = [[] for i in range(8)]
    expanded_RHS = expand(RHS)
    for i in range(len(expanded_RHS)):
        new_RHS[i // 6].append((expanded_RHS[i] + key[i]) % 2)

    for i in range(len(new_RHS)):
        new_RHS[i] = s_box(i, new_RHS[i])
        
    new_RHS = permute_key_array(flatten_key_matrix(new_RHS), final_f_perm)

    return new_RHS


def encrypt(plaintext, key):
    print("GENERATING THE ROUND KEYS:")
    round_keys = hex_key_to_round_keys(key)

    binary_plaintext = []
    for binary_digit in map(hex_to_binary, plaintext):
        binary_plaintext += binary_digit
    print("Plaintext in binary:", "".join(map(str, binary_plaintext)))

    binary_plaintext = permute_key_array(binary_plaintext, initial_perm)
    print("Plaintext after IP:", "".join(map(str, binary_plaintext)))

    LHS = binary_plaintext[:32]
    RHS = binary_plaintext[32:]
    print("L_0 = " + "".join(map(str, LHS)), "R_0 = " + "".join(map(str, RHS)))

    for i in range(len(round_keys)):
        old_LHS = list(LHS)
        LHS = list(RHS)
        partial_RHS = f(RHS, round_keys[i])
        for j in range(len(RHS)):
            RHS[j] = (old_LHS[j] + partial_RHS[j]) % 2
        print("L_" + str(i + 1) + " = " + "".join(map(str, LHS)), "R_" + str(i + 1) + " = " + "".join(map(str, RHS)))


    # Note we do RHS + LHS instead of LHS + RHS because on the last round the left and right sides aren't supposed
    # to be swapped, but they are swapped in the above loop. RHS + LHS just undoes the swap
    print("Binary cipher before applying P:", "".join(map(str, RHS + LHS)))
    binary_cipher_text = permute_key_array(RHS + LHS, initial_perm_inverse)

    print("Final binary cipher text:", "".join(map(str, binary_cipher_text)))

    return "".join(binary_to_hex(binary_cipher_text))



print("Plaintext:", plaintext, "Key:", key)
ciphertext = encrypt(plaintext, key)
print("Hex ciphertext:",ciphertext)