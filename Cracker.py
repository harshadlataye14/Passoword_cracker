import hashlib
import os
import re
import sys

print(
    """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                                                  
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                                                 
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                                                 
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                                                 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝                                                 
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                                                  
                                                                                                                                     
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║     ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                                                                                                                                                                              
"""
)

def check_hash_type(hash_value):
    if re.match(r'^[a-fA-F0-9]{32}$', hash_value):
        return "md5"
    elif re.match(r'^[a-fA-F0-9]{40}$', hash_value):
        return "sha1"
    elif re.match(r'^[a-fA-F0-9]{64}$', hash_value):
        return "sha256"
    else:
        print ("Unknown Hash Value")
        sys.exit()

def print_hash_type(hash_value):
    if re.match(r'^[a-fA-F0-9]{32}$', hash_value):
        print("Its MD5 Hash")
    elif re.match(r'^[a-fA-F0-9]{40}$', hash_value):
        print("Its SHA1 Hash")
    elif re.match(r'^[a-fA-F0-9]{64}$', hash_value):
        print("Its SHA256 Hash")
    else:
        print ("Unknown Hash Value")
        sys.exit()



def crack_passwords(hash_type, hash_value, password_file):
    with open(password_file, encoding="utf-8") as file:
        passwords = file.read().splitlines()

    for password in passwords:
        if hash_type == "md5":
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        elif hash_type == "sha1":
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type == "sha256":
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        else:
            print("Invalid hash type")
            return

        if hashed_password == hash_value:
            print(f"Password found: {password}")
            return

    print("Password not found in This Wordlist")

# Example usage
# hash_type = input("Enter the hash type (md5, sha1, sha256): ")
hash_value = input("Enter the hash value: ")
hash_type = check_hash_type(hash_value)
print_hash_type(hash_value)
password_file = input("Enter the password file path (or leave blank for default file): ")

print("""

██████╗ ██╗     ███████╗ █████╗ ███████╗███████╗    ██╗    ██╗ █████╗ ██╗████████╗            
██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔════╝    ██║    ██║██╔══██╗██║╚══██╔══╝            
██████╔╝██║     █████╗  ███████║███████╗█████╗      ██║ █╗ ██║███████║██║   ██║               
██╔═══╝ ██║     ██╔══╝  ██╔══██║╚════██║██╔══╝      ██║███╗██║██╔══██║██║   ██║               
██║     ███████╗███████╗██║  ██║███████║███████╗    ╚███╔███╔╝██║  ██║██║   ██║██╗██╗██╗██╗██╗
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
                                                                                              
""")

if not password_file:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = "password.txt"
    password_file = os.path.join(current_directory, file_name)

crack_passwords(hash_type, hash_value, password_file)