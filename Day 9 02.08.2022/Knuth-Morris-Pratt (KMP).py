txt = "abcdabcaaabc"

find = "abc"


def LPSArray(pat,m,lps):
    len = 0
    i = 1
    lps[0] = 0
    while i<m:
        if pat[i] == pat[len]:
            lps[i] = len + 1
            len+=1
            i+=1
        else:
            if len!=0:
                len = lps[len-1]
            else:
                lps[i]=0
                i+=1

def KMPSearch(pat,txt):
    N = len(txt)
    M = len(pat)
    lps = [0]*M
    LPSArray(pat,M,lps)
    i = 0
    j = 0
    while i < N-M+1:
        if txt[i]==pat[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
        if j==M:
            print(i-j)
            j = lps[j-1]

KMPSearch(find,txt)
