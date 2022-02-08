from graphics import*
from Button import*

#Converter Function
def Converter(value, currency):
    r = {"Euro" : 0.87,
        "Chinese Yuan" : 6.36,
        "Swiss Franc" :0.93,
        "Japanese Yen" : 115.23,
        "South Korean won":1198.39,
        "Canadian Dollar":1.28}
    if currency == "Euro":
        return round(value*r["Euro"],2)
    if currency == "Chinese Yuan":
        return round(value*r["Chinese Yuan"],2)
    if currency == "Swiss Franc":
        return round(value*r["Swiss Franc"],2)
    if currency == "Japanese Yen":
        return round(value*r["Japanese Yen"],2)
    if currency == "South Korean won":
        return round(value*r["South Korean won"],2)
    if currency == "Canadian Dollar":
        return round(value*r["Canadian Dollar"],2)
    


def main():

    #GUI frame
    win = GraphWin("Image Editor", 800, 600)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    Euro = Button(win, "white", "Euro", Point(720, 50), 45)
    Yuan = Button(win, "white", "Yuan", Point(720, 150), 45)
    Franc = Button(win, "white", "Franc", Point(720, 250), 45)
    JapaneseYen = Button(win, "white", "JapaneseYen", Point(720, 350), 60)
    KoreanWon = Button(win, "white", "KoreanWon", Point(720, 450), 60)
    CanadianDollar = Button(win, "white", "CanadianDollar", Point(720, 550), 60)

    #Input bar
    usinput = Text(Point(350,150),"Input your dollar below and choose a currency on the right")
    usinput.setSize(20)
    usinput.draw(win)
    e = Entry(Point(350,200),60)
    e.draw(win)
    
    #Output bar
    a1 = Text(Point(350,300),"Result")
    a1.setSize(20)
    a1.draw(win)

    m = win.getMouse()
    text = float(e.getText())
    word = Text(Point(350,350),"The value is ")
    word.setSize(20)
    word.draw(win)
    final = Text(Point(350,400),"")
    final.setSize(20)
    final.draw(win)

    #Clicked
    while True:
        if close.isClicked(m):
            break
        if Euro.isClicked(m):
            final.undraw()
            cu1 = "Euro"
            Value1 = str(Converter(text,cu1))
        if Yuan.isClicked(m):
            final.undraw()
            cu1 = "Chinese Yuan"
            Value1 = str(Converter(text,cu1))
        if Franc.isClicked(m):
            final.undraw()
            cu1 = "Swiss Franc"
            Value1 = str(Converter(text,cu1))
        if JapaneseYen.isClicked(m):
            final.undraw()
            cu1 = "Japanese Yen"
            Value1 = str(Converter(text,cu1))
        if KoreanWon.isClicked(m):
            final.undraw()
            cu1 = "South Korean won"
            Value1 = str(Converter(text,cu1))
        if CanadianDollar.isClicked(m):
            final.undraw()
            cu1 = "Canadian Dollar"
            Value1 = str(Converter(text,cu1))
            
        #Result    
        final = Text(Point(350,400),Value1)
        final.setSize(20)
        final.draw(win)
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
