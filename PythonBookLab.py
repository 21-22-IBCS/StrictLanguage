def main():
    f = open("Great.txt", "r")
    text = f.read()
    text.replace("\n"," ")
    list = text.split(" ")

    x = 0
    y = 0
    while not (list[x] == "In") and not (list[x+1] == "my"):
        x=x+1
    while not (list[y] == "***") and not (list[y+1] == "END"):
        y=y+1

    newlist = []
    for i in range(x,y):
        newlist.append(list[i])

    for word in range(len(newlist)):
        newlist[word] = newlist[word].replace(".","")
        newlist[word] = newlist[word].replace(",","")
        newlist[word] = newlist[word].replace("“","")
        newlist[word] = newlist[word].replace("”","")
        newlist[word] = newlist[word].replace(";","")
        newlist[word] = newlist[word].replace(":","")
        newlist[word] = newlist[word].replace("!","")
        newlist[word] = newlist[word].replace("?","")
                

        
    #average word length
    num = 0
    for word in newlist:
        num = num + len(word)
    print("The average word length is " + str(num/len(newlist)))


    #percentage of the conjunction and, but, or
    con = 0
    for i in range(len(newlist)):
        if newlist[i] == "and" or newlist[i] == "or" or newlist[i] == "but":
            con = con + 1
    average = con/len(newlist)*100
    print("The percentage of main coordinating conjunction is " + str(average)+"%")
    

if __name__ == "__main__":
    main()
