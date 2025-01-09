class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        prefLength=len(pref)
        for i in range (len(words)):
            word=words[i]
            prefTest=word[0:prefLength]
            if(prefTest.lower()==pref.lower() ):
                count+=1
        print(count)



solution=Solution()
solution.prefixCount(words = ["leetcode","win","loops","success"], pref = "code")
#print(answer)