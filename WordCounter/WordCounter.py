class WordCounter :
    def __init__(self,words):
        self.words  = words.lower().split(" ")
        self.unique_words =[]
        self.counts =[]
    
    def count_words(self):
        for word in self.words:
            if word  in self.unique_words:
                index = self.unique_words.index(word)
                self.counts[index] +=1
            else:
                self.unique_words.append(word)
                self.counts.append(1)
    def display_words(self):
        for i in range(len(self.unique_words)):
            print(f"{self.unique_words[i]} -> {self.counts[i]}")