##########################################################
#########################################################

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: 
"a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Morse code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]




Return the number of different transformations among all words we have.




########## solution

 def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        index = 0
        count = collections.Counter()
        tlist = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letterlist = [chr(i) for i in range(97, 123)]
        tdict = {}
        for x in letterlist:
            tdict[x] = tlist[index]
            index += 1
        
        for x in words:
            x = "".join(str(""+ tdict.get(n)) for n in x)
            count[x]+=1
            
        return len(dict(count))



