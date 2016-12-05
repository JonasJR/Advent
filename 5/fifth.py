import hashlib

password = ""
new_pass = {}
used = []

def put_char(char,poss):
    global new_pass
    if poss.isdigit() and 0 <= int(poss) <= 7:
        if poss not in new_pass:
            new_pass[poss] = char
            print(poss)

def main():
    global password
    stringen = "ojvtpuvg"
    counter = 0
    temp = ""
    m = hashlib.md5()
    while True:
        temp = stringen + str(counter)
        hash_object = hashlib.md5(temp.encode())
        hashed = hash_object.hexdigest()
        if hashed[:5] == "00000":
            position = hashed[5]
            char = hashed[6]
            put_char(char, position)
            #password += password.join(hashed[5])
        if len(new_pass) == 8:
            break
        counter += 1
    print(new_pass)

main()
