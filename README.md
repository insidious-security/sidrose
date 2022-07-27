# SidRose

This code can be used to encrypt and decrypt small files and directories limited to 2GB in file size.
The python module used is Fernet, symetric encryption.

## Usage:
```bash
# Execute this source in the directory of which you want to encrypt the contents.
$ python3 sidrose.py 

# Follow the instructions in the cli:

 ███████╗██╗██████╗ ██████╗  ██████╗ ███████╗███████╗
 ██╔════╝██║██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝
 ███████╗██║██║  ██║██████╔╝██║   ██║███████╗█████╗
 ╚════██║██║██║  ██║██╔══██╗██║   ██║╚════██║██╔══╝
 ███████║██║██████╔╝██║  ██║╚██████╔╝███████║███████╗
 ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                       (1): Encrypting
                       (2): Decrypting

:

# Make sure NOT to delete the "very-special-key", you'll need this to decrypt the data again.
# The key is random generated and can be used only for the encypted contents its been created for.

Please note: 
# When using this code on larger directories then specified above this program wil not act as intended, use with caution.
```
