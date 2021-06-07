

if __name__ == "__main__":
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    # first clean blank char
    remap = {
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None,
    }
    a = s.translate(remap)
    print(a)
    
    # second remove note
    import unicodedata
    import sys
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a).translate(cmb_chrs)
    print(b)