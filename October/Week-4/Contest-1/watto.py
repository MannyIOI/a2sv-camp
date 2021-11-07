class Trie:
    def __init__(self):
        self.children = [0] * 26
        self.is_end = False


    def addWord(self, word):
        curr = self
        for i in word:
            if not curr.children[ord(i) - 97]:
                node = Trie()
            else:
                node = curr.children[ord(i) - 97]
            curr.children[ord(i) - 97] = node
            curr = node
        curr.is_end = True
        return self

    def search(self, word, error=0, position=0):
        if error > 1:
            return False
        if position == len(word):
            return self.is_end
        elif position > len(word):
            return False
        
        ans = False
        pos = ord(word[position]) - 97
        # if self.children[pos]:
        #     ans = self.children[pos].search(word, error, position + 1)
        for i in range(len(self.children)):
            x = self.children[i]
            if x:
                new_err = error
                if i != pos:
                    error += 1
                ans = ans or x.search(word, error + 1, position + 1)

        return ans
        

trie = Trie()
# trie.addWord('aaaaa')
# print(trie.search('aabba'))

n, m = [int(i) for i in input().split()]
for i in range(n):
    word = input()
    trie.addWord(word)

for i in range(m):
    word = input()
    ans = trie.search(word)
    if ans:
        print('YES')
    else:
        print('NO')