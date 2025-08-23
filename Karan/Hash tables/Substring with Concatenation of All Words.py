class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words: return []
        word_len=len(words[0])
        total_len=word_len*len(words)
        word_count={}
        for w in words:
            word_count[w]=word_count.get(w,0)+1
        res=[]
        for i in range(word_len):
            left=i
            count=0
            seen={}
            for j in range(i,len(s)-word_len+1,word_len):
                w=s[j:j+word_len]
                if w in word_count:
                    seen[w]=seen.get(w,0)+1
                    count+=1
                    while seen[w]>word_count[w]:
                        left_word=s[left:left+word_len]
                        seen[left_word]-=1
                        left+=word_len
                        count-=1
                    if count==len(words):
                        res.append(left)
                else:
                    seen.clear()
                    count=0
                    left=j+word_len
        return res