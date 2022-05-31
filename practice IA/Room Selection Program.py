from graphics import*
from Button import*

def main():

    win = GraphWin("Room Selection",1300,800)
    
    map = Image(Point(500,450), "map.png")
    map.draw(win)


    title = Text(Point(650,20), "Room Selection Program") 
    title.setSize(32)
    title2 = Text(Point(400,80), "Map")
    title2.setSize(28)
    title.draw(win)
    title2.draw(win)

    name = Text(Point(1100,150), "Enter name")
    name.draw(win)
    name.setSize(25)
    roomnum = Text(Point(1100,250), "Enter your room number")
    roomnum.draw(win)
    roomnum.setSize(25)

    error = Text(Point(1000,520), "This room has already been selected!")
    error.setSize(28)
    error.setFill("red")

    error2 = Text(Point(1000,520), "Successful changed room!")
    error2.setSize(18)
    error2.setFill("red")
    
    fun = Entry(Point(1100,200),30)
    fun.draw(win)
    fun1 = Entry(Point(1100,300),30)
    fun1.draw(win)

    confirm = Button(win, 'white', "Confirm", Point(1100,400), 75)
    undo = Button(win, 'red', "UNDO", Point(1100,50), 50)


    

    data = {}

    empty = Text(Point(800,670), "No student select room yet!")
    empty.setSize(25)
    empty.setFill("red")

    roominfo = Text(Point(650,700), data)
    roominfo.setSize(15)

    
    while True:
        m1 = win.getMouse()
        if confirm.isClicked(m1):
            error.undraw()
            error2.undraw()
            empty.undraw()
            roominfo.undraw()
            f = fun.getText()
            f1 = fun1.getText()
            c = 0
            for i in data.keys():
                if f1 == data[i]:
                    error.draw(win)
                    c = 1
                if f == i and f1 != data[i]:
                    error2.draw(win)

            if c == 0:
                data[f] = f1


            roominfo.draw(win)
            print(data)
            fun.setText('')
            fun1.setText('')


        if undo.isClicked(m1):
            error.undraw()
            error2.undraw()
            empty.undraw()
            roominfo.undraw()
        
            if len(data) != 0:
                data.popitem()
                print(data)
            else:
                empty.draw(win)
            roominfo.draw(win)

       
                        
            
                
                
    

if __name__ == "__main__":
    main()
