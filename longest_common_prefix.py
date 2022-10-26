strs=["flower","flow","flight"]
def get_the_prefix():
    output=""
    same_letter=True
    x=0
    while same_letter==True and x<len(min(strs)):
        letter=strs[0][x]
        for str in strs:
            if str[x]==letter:
                pass
            else:
                same_letter=False
                break
        if same_letter:
            output+=str[x]
            x+=1
    return output
print(get_the_prefix())