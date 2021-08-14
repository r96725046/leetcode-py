#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
   # ***
   # 1.i is the next word, not in this line
   # 2.while i<=arr.length,don't use String word=words[i] ***
   # 3.Check Length 
   #   a.i==arr.length ***
   #   b.count + i-index-1 + 1 space + word.length() ***
   # 4.Left Justification
   # 5 Middle Justification
   #   a.slot = i-index-1
   #   b.space = max-count/slot
   #   c.extra = max-count%slot
   # 6.if i<length, count=words[i].length()
   # 7.else count+=words[i].length()
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res=[]
        i=0
        count=0
        pre=0
        while i in range(len(words)+1):
            if i==len(words) or count+(i-pre)+len(words[i])>maxWidth:
                #left justification
                tmp=""
                if i==len(words) or i-pre==1:
                    for j in range(pre,i):
                        if j>pre:
                            tmp+=" "
                        tmp+= words[j]
                    if len(tmp)<maxWidth:
                        while len(tmp)<maxWidth:
                            tmp+=" "
                #middle justification
                else:
                    space = (maxWidth-count)//(i-pre-1)
                    extra = (maxWidth-count)%(i-pre-1)
                    for j in range(pre,i):
                        tmp+=words[j]
                        if j<i-1:
                            for k in range(space):
                                tmp+=" "
                            if extra>0:
                                tmp+=" "
                                extra-=1
                res.append(tmp)
                if i<len(words):
                    count=len(words[i])
                pre=i
            else:
                count+=len(words[i])
            i+=1
        return res

# @lc code=end

