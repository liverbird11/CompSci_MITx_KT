## Encryption: Simple Cipher and Decryptor

This simple Python program is created from a problem set (pset5) in the course [Introduction to Computer Science and Programming using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7) by MITx, which I attended from Jan-Mar 2020.

The code is as-submitted + a couple of functions added to allow custom encryption and decryption of your own messages.

**Caution**: This is a very simple encryptor and the ciphertext can be easily decrypted by brute force, as you can see by running the decryptor function in this code yourself!

#### Running the code

Start by running _ps5.py_ in your chosen IDE (e.g. Spyder).

To use the decryptor to decrypt a secret message from the MITx course given in _story.txt_:

```
decrypt_story()
```

To encrypt a secret message and have it saved in _EncryptedMessage.txt_. Please remember to include quotation marks in your message("example" or 'example'), and _shift_ is an integer (from 1 to 25) denoting the number of letters to shift to generate the ciphertext:

```
encrypt_story("This is an example message", shift)
```

To decrypt the ciphertext in _EncryptedMessage.txt_:

```
CiphertextMessage(get_message_string("EncryptedMessage.txt")).decrypt_message()
```

The above returns an integer given by (26 - _shift_), followed by the decrypted message.