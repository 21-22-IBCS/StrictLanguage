from graphics import*
from Button import*
from math import*

def calcy(f, num):
    if "+" in f:
        l = f.split("+")
        result = 0
        for j in l:
            result = result + calcy(j,num)
        return result
    elif "-" in f:
        l = f.split("-")
        result = calcy(l[0],num)-calcy(l[1],num)
        return result
    elif "*" in f:
        l = f.split("*")
        result = 1
        for j in l:
            result = result * calcy(j,num)
        return result
    elif "/" in f:
        l = f.split("/")
        result = calcy(l[0],num)/calcy(l[1],num)
        return result
    elif "e^x" in f:
        return e**num
    elif "^" in f:
        l = f.split("^")
        result = pow(calcy(l[0],num),calcy(l[1],num))
        return result
    elif "sqrt(x)" in f:
        return sqrt(num)
    elif "sin(x)" in f:
        return sin(num)
    elif "cos(x)" in f:
        return cos(num)
    elif "log(x)" in f:
        return log(num)
    elif "x" in f:
        return num
    else:
        return float(f)

        l = f.split("-")
        result = calcy(l[0],num)-calcy(l[1],num)
def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function you would like to graph")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)
    for i in range(1,6):
        XPnum = Text(Point(400+i*50,410),i)
        XNnum = Text(Point(400-i*50,410),"-"+str(i))
        YPnum = Text(Point(390,400-i*50),i)
        YNnum = Text(Point(390,400+i*50),"-"+str(i))
        XPnum.draw(win)
        XNnum.draw(win)
        YPnum.draw(win)
        YNnum.draw(win)
    num0 = Text(Point(395,410),"0")
    num0.draw(win)
    
    yAxis = Line(Point(400,150), Point(400,600))
    yAxis.draw(win)
    xAxis = Line(Point(100,400), Point(700,400))
    xAxis.draw(win)

    funText = Text(Point(200,650), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,650),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(550,650), 75)
    quitB = Button(win, 'red', "QUIT", Point(400,720), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()

            scale = 50
            points = []

            if "sqrt(x)" in f:
                for i in range (0,250):
                    x = i+400
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))
            elif "log(x)" in f:
                for i in range (1,250):
                    x = i+400
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))      
            else:
                for i in range(-250,250):
                    x = i+ 400
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))

            for p in points:
                p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break
                
    

if __name__ == "__main__":
    main()
