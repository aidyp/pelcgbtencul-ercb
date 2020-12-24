import codecs

def to_chr(hex_string):
    '''
    Takes in a hex string and returns it as characters
    '''
    decode_hex = codecs.getdecoder("hex_codec")
    return decode_hex(hex_string)[0]


def pack_for_cat(content)
    '''
    Takes in the content as a dictionary
    Packs it for use with netcat
    '''
    package = str(content).replace("\'", "\"")
    return package