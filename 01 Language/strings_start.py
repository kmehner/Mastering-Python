# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them. This will cause ean error:
        # TypeError: can only concatenate str (not "bytes") to str
        # The print statement expects a str although they equate to the same value
    # print(s+b)

    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    # since we know it is utf-8, we can use the decode/encode function
        # otherwise we would need to perform detection logic 

    # DECODE converts the string to bytes 
    # ENCODE conveerts the bites to a string
    
    # TODO: decode the string and encode the byte as utf-8
    s2 = b.decode('utf-8')
    print(s+s2)

    b2 = s.encode('utf-8')
    print(b + b2)
    
    # TODO: encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)
    
if __name__ == "__main__":
    main()
