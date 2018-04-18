
'''
This will NOT run in repl.it or SoloLearn Code Playground!
it's just an easy way for people to access, edit, and reuse this code.
(And if you do use this for yourself please give some credit!)
                                                                                           
This will run in both Python 2.7 and Python 3.6.                                               
Please run in Terminal/CMD for best results.                                                   
                                                                                        
This requires a text file called "Text.txt" or you may change the variable "Text.txt" to the name of your text file on both instances.
With the first line being your desired Username and the second being an MD5 Hash of the desired Password.

If you are having trouble with what to put in the text file here is an example.
 __________________________________________
|O_O_O_____________________________________|
|Bob                                       |
|e10adc3949ba59abbe56e057f20f883e          |
|                                          |
|                                          |   
|                                          |    
|__________________________________________|

In this instance the username is "Bob" and the password is "123456".

If you are still confuzed in the long string of letters and numbers, it is called an MD5 Hash. It is a way of protecting Passwords from Hackers.
In my example it changes "123456" into "e10adc3949ba59abbe56e057f20f883e". 
The login program then converts the Password you enter to MD5 form and compares them. (This is called Checksum.)

Feel free to add this to any of your own python creation with need of a secure login! <3 But if you do this you HAVE TO GIVE US MONEY AND YOU WILL BECOME A SCRIPT KIDDIE

'''
import getpass, os
def login():
        #For Mac Users change the 'cls' to 'clear'.
        os.system('clear')
        print(' ---------- Welcome to RougeOSL Version 1.0.0  ----------- \n           (SOON TO BE INTEGRATED WITH S.A.T.O)')
        username = raw_input("Username:      ")
        #getpass.getpass doesn't show the input as the user types it, instead it shows no input at all.
        password = getpass.getpass('Password:      ')
        #Reads line 1 of the file.
        def User():
                #One instance of the filename here!
                with open('Text.txt') as f:
                        x = 0
                        #xrange evaluates lazily and takes up less memory.
                        for i in xrange(3):
                                line = f.readline();
                                x += 1
                                if x == 1:
                                        return line.split()
        #Reads line 2 of the file.
        def Pass():
                #Another instance here!
                with open('Text.txt') as f:
                        x = 0
                        for i in xrange(3):
                                line = f.readline();
                                x += 1
                                if x == 2:
                                        return line.split()
        #This is where the program converts the Password to MD5 Hashed form.
        def MD5_Hash(password):
            qwerty = password
            hexcase = 0;	
            b64pad	= ""; 
            chrsz	 = 8;	
            intlenbit = 32 
            hex_md5 = lambda s: binl2hex(core_md5(str2binl(s), len(s) * chrsz))
            def binl2hex(binarray):
                    if hexcase == 1:
                            hex_tab = "0123456789ABCDEF"
                    else: 
                            hex_tab = "0123456789abcdef"
                    str = ""
                    i = 0
                    while i < len(binarray) * 4:
                            str += hex_tab[(binarray[i>>2] >> ((i % 4) * 8 + 4)) & 0xF] + hex_tab[(binarray[i>>2] >> ((i % 4) * 8)) & 0xF]
                            i+=1
                    return str
            def str2binl(str):
                    bin = {}
                    mask = (1 << chrsz) - 1
                    i = 0
                    while i < len(str) * chrsz:
                            ind = i >> 5
                            sdv = i % intlenbit
                            str_c = ord(str[int(i/chrsz)]) & mask
                            bin[ind] = bin.get(ind,0) | str_c << sdv
                            i+=chrsz
                    return bin
            def safe_add(x, y):
                    lsw = (x & 0xFFFF) + (y & 0xFFFF)
                    msw = (((x & (2**intlenbit - 1)) >> 16) + ((y & (2**intlenbit - 1)) >> 16)	+ (lsw >> 16)) & (2**intlenbit - 1)
                    return ((msw << 16) | (lsw & 0xFFFF)) & (2**intlenbit - 1)
            rol = lambda num, cnt:\
                    ((num << cnt % intlenbit) & (2**intlenbit - 1))\
                    | (((num & (2**intlenbit - 1)) >> (intlenbit - cnt % intlenbit)) & (2**intlenbit - 1))
            md5_cmn = lambda q, a, b, x, s, t: safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s),b)
            md5_ff = lambda a, b, c, d, x, s, t: md5_cmn((b & c) | ((~b) & d), a, b, x, s, t)
            md5_gg = lambda a, b, c, d, x, s, t: md5_cmn((b & d) | (c & (~d)), a, b, x, s, t)
            md5_hh = lambda a, b, c, d, x, s, t: md5_cmn(b ^ c ^ d, a, b, x, s, t)
            md5_ii = lambda a, b, c, d, x, s, t: md5_cmn(c ^ (b | (~d)), a, b, x, s, t)	
            def core_md5(x, l):
                    x[l >> 5] |= 0x80 << ((l) % 32)
                    x[(((l + 64) >> 9) << 4) + 14] = l 
                    a, b, c, d, i =	1732584193, -271733879, -1732584194, 271733878, 0
                    while i < len(x):
                            olda, oldb, oldc, oldd	= a, b, c, d
                            a = md5_ff(a, b, c, d, x.get(i+ 0, 0), 7 , -680876936)
                            d = md5_ff(d, a, b, c, x.get(i+ 1, 0), 12, -389564586)
                            c = md5_ff(c, d, a, b, x.get(i+ 2, 0), 17,	606105819)
                            b = md5_ff(b, c, d, a, x.get(i+ 3, 0), 22, -1044525330)
                            a = md5_ff(a, b, c, d, x.get(i+ 4, 0), 7 , -176418897)
                            d = md5_ff(d, a, b, c, x.get(i+ 5, 0), 12,	1200080426)
                            c = md5_ff(c, d, a, b, x.get(i+ 6, 0), 17, -1473231341)
                            b = md5_ff(b, c, d, a, x.get(i+ 7, 0), 22, -45705983)
                            a = md5_ff(a, b, c, d, x.get(i+ 8, 0), 7 ,	1770035416)
                            d = md5_ff(d, a, b, c, x.get(i+ 9, 0), 12, -1958414417)
                            c = md5_ff(c, d, a, b, x.get(i+10, 0), 17, -42063)
                            b = md5_ff(b, c, d, a, x.get(i+11, 0), 22, -1990404162)
                            a = md5_ff(a, b, c, d, x.get(i+12, 0), 7 ,	1804603682)
                            d = md5_ff(d, a, b, c, x.get(i+13, 0), 12, -40341101)
                            c = md5_ff(c, d, a, b, x.get(i+14, 0), 17, -1502002290)
                            b = md5_ff(b, c, d, a, x.get(i+15, 0), 22,	1236535329)
                            a = md5_gg(a, b, c, d, x.get(i+ 1, 0), 5 , -165796510)
                            d = md5_gg(d, a, b, c, x.get(i+ 6, 0), 9 , -1069501632)
                            c = md5_gg(c, d, a, b, x.get(i+11, 0), 14,	643717713)
                            b = md5_gg(b, c, d, a, x.get(i+ 0, 0), 20, -373897302)
                            a = md5_gg(a, b, c, d, x.get(i+ 5, 0), 5 , -701558691)
                            d = md5_gg(d, a, b, c, x.get(i+10, 0), 9 ,	38016083)
                            c = md5_gg(c, d, a, b, x.get(i+15, 0), 14, -660478335)
                            b = md5_gg(b, c, d, a, x.get(i+ 4, 0), 20, -405537848)
                            a = md5_gg(a, b, c, d, x.get(i+ 9, 0), 5 ,	568446438)
                            d = md5_gg(d, a, b, c, x.get(i+14, 0), 9 , -1019803690)
                            c = md5_gg(c, d, a, b, x.get(i+ 3, 0), 14, -187363961)
                            b = md5_gg(b, c, d, a, x.get(i+ 8, 0), 20,	1163531501)
                            a = md5_gg(a, b, c, d, x.get(i+13, 0), 5 , -1444681467)
                            d = md5_gg(d, a, b, c, x.get(i+ 2, 0), 9 , -51403784)
                            c = md5_gg(c, d, a, b, x.get(i+ 7, 0), 14,	1735328473)
                            b = md5_gg(b, c, d, a, x.get(i+12, 0), 20, -1926607734)
                            a = md5_hh(a, b, c, d, x.get(i+ 5, 0), 4 , -378558)
                            d = md5_hh(d, a, b, c, x.get(i+ 8, 0), 11, -2022574463)
                            c = md5_hh(c, d, a, b, x.get(i+11, 0), 16,	1839030562)
                            b = md5_hh(b, c, d, a, x.get(i+14, 0), 23, -35309556)
                            a = md5_hh(a, b, c, d, x.get(i+ 1, 0), 4 , -1530992060)
                            d = md5_hh(d, a, b, c, x.get(i+ 4, 0), 11,	1272893353)
                            c = md5_hh(c, d, a, b, x.get(i+ 7, 0), 16, -155497632)
                            b = md5_hh(b, c, d, a, x.get(i+10, 0), 23, -1094730640)
                            a = md5_hh(a, b, c, d, x.get(i+13, 0), 4 ,	681279174)
                            d = md5_hh(d, a, b, c, x.get(i+ 0, 0), 11, -358537222)
                            c = md5_hh(c, d, a, b, x.get(i+ 3, 0), 16, -722521979)
                            b = md5_hh(b, c, d, a, x.get(i+ 6, 0), 23,	76029189)
                            a = md5_hh(a, b, c, d, x.get(i+ 9, 0), 4 , -640364487)
                            d = md5_hh(d, a, b, c, x.get(i+12, 0), 11, -421815835)
                            c = md5_hh(c, d, a, b, x.get(i+15, 0), 16,	530742520)
                            b = md5_hh(b, c, d, a, x.get(i+ 2, 0), 23, -995338651)
                            a = md5_ii(a, b, c, d, x.get(i+ 0, 0), 6 , -198630844)
                            d = md5_ii(d, a, b, c, x.get(i+ 7, 0), 10,	1126891415)
                            c = md5_ii(c, d, a, b, x.get(i+14, 0), 15, -1416354905)
                            b = md5_ii(b, c, d, a, x.get(i+ 5, 0), 21, -57434055)
                            a = md5_ii(a, b, c, d, x.get(i+12, 0), 6 ,	1700485571)
                            d = md5_ii(d, a, b, c, x.get(i+ 3, 0), 10, -1894986606)
                            c = md5_ii(c, d, a, b, x.get(i+10, 0), 15, -1051523)
                            b = md5_ii(b, c, d, a, x.get(i+ 1, 0), 21, -2054922799)
                            a = md5_ii(a, b, c, d, x.get(i+ 8, 0), 6 ,	1873313359)
                            d = md5_ii(d, a, b, c, x.get(i+15, 0), 10, -30611744)
                            c = md5_ii(c, d, a, b, x.get(i+ 6, 0), 15, -1560198380)
                            b = md5_ii(b, c, d, a, x.get(i+13, 0), 21,	1309151649)
                            a = md5_ii(a, b, c, d, x.get(i+ 4, 0), 6 , -145523070)
                            d = md5_ii(d, a, b, c, x.get(i+11, 0), 10, -1120210379)
                            c = md5_ii(c, d, a, b, x.get(i+ 2, 0), 15,	718787259)
                            b = md5_ii(b, c, d, a, x.get(i+ 9, 0), 21, -343485551)
                            a, b, c, d = safe_add(a, olda), safe_add(b, oldb), safe_add(c, oldc), safe_add(d, oldd)
                            i+=16
                    return {0:a,1:b,2:c,3:d}
            sArr = [(qwerty)];
            for s in sArr:
                return str(hex_md5(s))
        a = User()
        b = Pass()
        c = MD5_Hash(password)
        def CorrectUser():
                if str(a[0]) == username:
                        return ('Correct User')
                else:
                        return ('Wrong User')
        def CorrectPass():
                if str(b[0]) == str(c):
                        return ('Correct Password')
                else:
                        return ('Wrong Password')
        s,t = CorrectUser(),CorrectPass()
        return '\n'+s+'\n'+t
x = login()
#When you print x it will return weather or not the user had the correct Username and Password. (It also calls the entire program to run!)
print (x)
