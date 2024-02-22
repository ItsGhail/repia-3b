import streamlit as st

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""
    
    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        cipher_byte = plaintext_byte ^ key_byte
        ciphertext.append(cipher_byte)
        
        print(f"Plaintext byte: {bin(plaintext_byte)[2:]:>08} = {chr(plaintext_byte)}")
        print(f"Key byte:       {bin(key_byte)[2:]:>08} = {chr(key_byte)}")
        print(f"XOR result:     {bin(cipher_byte)[2:]:>08} = {chr(cipher_byte)}")
        print("-" * 20)
        
   
    return ciphertext

def xor_decrypt(ciphertext, key):
   
    """Decrypt ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key) # XOR decription is the same as encryption

# Example usage:
plaintext = bytes(st.text_area("Plaintext:").encode())
key = bytes(st.text_area("key:").encode())

if st.button("Encrypt!"):
    if len(plaintext) >= len(key):
    if plaintext != key:
        cipher = xor_encrypt(plaintext, key)
        print("Ciphertext:", "".join([f"{chr(byte_val)}" for byte_val in cipher]))
        
        decrypt = xor_decrypt(cipher, key)
        print("Decrypted:", "".join([f"{chr(byte_val)}" for byte_val in decrypt]))
    else:
        print("Plaintext should not be equal to the key")
else:
    print("Plaintext length should be equal or greater than the length of key")
