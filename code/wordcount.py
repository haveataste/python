def processLine(line,wordCounts):
    line=replacePunctuations(line)
    words=line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1

def replacePunctuations(line):
    for ch in line:
        if ch in "~!@#$%^&*()_-+=<>?/,.:;'""":
            line=line.replace(ch," ")
    return line

def main():
    str=input()
    wordCounts={}
    processLine(str.lower(),wordCounts)
    pairs=list(wordCounts.items())
    print(pairs)
    items=[[x,y] for (y,x) in pairs]
    print(items)
    items.sort()
    print(items[-1][1])

if __name__ == "__main__":
    main()
            
