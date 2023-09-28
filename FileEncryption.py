infile=open('info_security.txt','r')
outfile=open('encrypted.txt','w')
cycpher= {'A':'1','a':'!','B':'2','b':'@','C':'3','c':'<','D':'4','d':'$','E':'5','e':'%','F':'6','f':'^','G':'7','g':'&','H':'8','h':'*','I':'9','i':'>','J':'0','j':'/','K':',','k':'.','L':']','l':'[','M':'}','m':'{','N':'-','n':'_','O':'+','o':'=','P':';','p':'~','Q':'`','q':"'",'R':'"','r':'(','S':')','s':'#','T':'11','t':'1!','U':'2@','u':'22','V':'33','v':'3#','W':'44','w':'4$','X':'55','x':'5%','Y':'66','y':'6^','Z':'77','z':'7&'}
print(cycpher)

read=infile.readline()


for i in read:
    if i in cycpher:
        
        i=cycpher[i]
        outfile.write(i)
        
    else:
        outfile.write(i)
        
    


infile.close()