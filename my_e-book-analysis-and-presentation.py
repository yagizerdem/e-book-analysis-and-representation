import requests 
from bs4 import BeautifulSoup
from itertools import islice

def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))

# Url creating region
def createUrl(Book_Name):
    Url = "https://en.wikibooks.org/wiki/"
    Book_Name.replace(" ", "_").replace("'" , "%27") 
    FullUrl = Url + Book_Name + "/Print_version" 
    return FullUrl
# Region end

# Write books text to a file.txt
def CreateFiletxt(File_Name , script):
    File_Name = open("{File_Name}".format(File_Name=File_Name), "w",encoding='utf-8')
    File_Name.write(script)
# Region end
# Write words to a file.txt
def CreateFile_wordstxt(File_Name , wordlist):
    File_Name = open("{File_Name}".format(File_Name=File_Name), "w",encoding='utf-8')
    for word in wordlist:
        if(word != " " and word != ""):
            File_Name.write(word+"\n")
    File_Name.close()                        
# Region end

# Removing unnecessary words
def Remove_Words(words):
    Stop_Words= ["etc", "us", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "r",'s',
                 "u", "v", "y", "z", "w", "x", "q", "I", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                 "your", "yours","yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", '>' , '<','←',
                 "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves","what", "which",'↑',
                 "who", "whom", "this", "that", "these", "those", "am", "is", "are","was", "were", "be", "been",'→', 
                 "being", "have", "has", "had", "having", "do", "does", "did","doing", "a", "an", "the", "and", "but",
                 "if", "or", "because", "as", "until", "while", "of","at", "by", "for", "with", "about", "against",
                 "name","value","next","first", "between", "into", "through", "during", "before","after", "above",
                 "below", "to", "from", "up","line", "down", "in", "out", "on", "off", "over", "under","'ll", "'ve", "'re",
                 "again", "further", "then","ing", "once", "here", "there", "when", "where", "why", "how", "all", "any",
                 "both", "each", "few", "more", "most", "other","use", "some", "such", "no", "nor", "not", "only", "own",
                 "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","'m", "'s", "'t", 
                 '—', '=', '==', '\t', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.' , ',' , '!' ,'?','(',')' ,';',
                 '[', ']', '\n' , '"' , ':' , '-', '  ' , '~' , '@' , '^' , '#' , '%' , '$' , '&' , '*' , '_' ,'`' , '{' , '}' , '|']
    isOk = True
    Filterd_words = []
    for word in words:
        for item in Stop_Words:
            if item == word:
              isOk = False
              break    
        if(isOk):
          Filterd_words.append(word)
        isOk=True
    return Filterd_words
# Region end

# Removing punctuation
def Remove_Punctuation(words):
    Punctuation ='!"#$%&()*, -./:;<=>?@[\]^_`{|}~0123456789'+"'"
    Filterd_words=[]
    for word in words:
        for item in Punctuation:
            word = word.replace(item,"")
        Filterd_words.append(word)
    words = Filterd_words
    return words        
# Region end

# Creating dictionary
def Dictionary(words):
    dic = {}
    for word in words:
        if(word in dic.keys()):
            count = dic["{}".format(word)]
            count = count+1
            dic["{}".format(word)]=count
        else:
            dic["{}".format(word)]=1
    
    return dic
#

# Main region
while True:
    print(">>Enter 1 to get 1 book word frequency")
    print(">>Enter 2 to get 2 books common word frequence")
    print(">>Enter 3 to exit")

    user_input = int(input("Enter option :"))

    if user_input == 1:
        # user entering word frequence
        IsCustom_Frequence = input("User input for custom word frequence. Enter Y or N :")
        if(IsCustom_Frequence == "Y"):
            Word_Frequency = int(input("Enter word frequence :"))
        else:
            Default_Word_Frequency = 20
            Word_Frequency = Default_Word_Frequency    
        # Region end
        Book_Name = input("Please enter your desired book name: ")
        FullUrl =createUrl(Book_Name)
        #Scrapping web data 
        html = requests.get(FullUrl).content
        soup = BeautifulSoup(html , "html.parser")
        script = soup.find("div",{"class":"mw-parser-output"}).text.lower()
        # Region end
        CreateFiletxt("Book1_txt.txt" , script)
        #Gettings words in script text file
        words = script.split()
        words = Remove_Words(words)
        words = Remove_Punctuation(words)
        CreateFile_wordstxt("Book1_words_txt.txt" , words)
        # Region end
        # Printing words on console
        dic =Dictionary(words)
        dic = take(Word_Frequency, dic.items())
        print("words ----- Frequence")
        for key,values in dic:
            print(str(key)  + "     " +str(values))
        #
    if user_input == 2:
         # user entering word frequence
        IsCustom_Frequence = input("User input for custom word frequence. Enter Y or N :")
        if(IsCustom_Frequence == "Y"):
            Word_Frequency = int(input("Enter word frequence :"))
        else:
            Default_Word_Frequency = 20
            Word_Frequency = Default_Word_Frequency
        # Region end     
        Book_Name = input("Please enter your desired book name: ")
        FullUrl =createUrl(Book_Name)
        #Scrapping web data 
        Book_Name2 = input("Please enter your desired book name: ")
        FullUrl2 =createUrl(Book_Name2)

        html = requests.get(FullUrl).content
        soup = BeautifulSoup(html , "html.parser")
        script = soup.find("div",{"class":"mw-parser-output"}).text.lower()

        html2 = requests.get(FullUrl2).content
        soup2 = BeautifulSoup(html2 , "html.parser")
        script2 = soup2.find("div",{"class":"mw-parser-output"}).text.lower()
        # Region end
        CreateFiletxt("Book1_txt.txt" , script)
        CreateFiletxt("Book2_txt.txt" , script2)
        #Gettings words in script text file
        words = script.split()
        words = Remove_Words(words)
        words = Remove_Punctuation(words)
        CreateFile_wordstxt("Book1_words_txt.txt" , words)

        words2 = script2.split()
        words2 = Remove_Words(words2)
        words2 = Remove_Punctuation(words2)
        CreateFile_wordstxt("Book2_words_txt.txt" , words2)
        #Region end
        # Printing words on console
        dic =Dictionary(words)
        dic2 = Dictionary(words2)
        dic3={}

        for item in dic.keys():
            for item2 in dic2.keys():
                if(item==item2):
                    dic3["{}".format(item)] = dic["{}".format(item)] + dic2["{}".format(item2)]    
        dic = take(Word_Frequency, dic3.items())
        print("words ----- Frequence")
        for key,values in dic:
            print(str(key)  + "     " +str(values))
        # Region end
    if user_input == 3:
        print("logged out")
        break

# Main region end
