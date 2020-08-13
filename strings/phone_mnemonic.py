# the mapping from digit to corresponding characters
mapping = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number):
    # recursion function
    def mnemonic_recursor(digit):
        #base case 
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        #recursion
        else:
            #recursing over all characters in each phone number index
            for c in mapping[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                mnemonic_recursor(digit + 1)
    
    #initialize return array and copy of it for each branch
    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    mnemonic_recursor(0)
    return mnemonics

print(phone_mnemonic('626'))

# Time complexity: O(4^n * n) - four symbols in a 1 single digit + O(n) at the base case because of str.join(array)
# Space complexity: O(n) - mnemonics list