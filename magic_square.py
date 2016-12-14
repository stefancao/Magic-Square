#File: magic_square.py
#Name: Stefan Cao
#Date: 23 November 2013
#Course: EECS 12 - Introduction to Programming
#Description: Magic Square

from graphics import*
import time

#Function for flying object from start x,y to end x,y
def move(obj, startX, startY, endX, endY):
    X = (endX-startX)/10
    Y = (endY-startY)/10
    for i in range(10):
        obj.move(X,Y)
        time.sleep(0.05)

#Function for calculating the actual (x, y) coord given (column, row)
def calculateCoordinates (left_end, top_end, cell_width, column, row):
    x_coord = left_end.x + (cell_width/2) + (cell_width*(column-1))
    y_coord = left_end.y - (cell_width/2) - (cell_width*(row-1))
    return x_coord, y_coord
            

def main():
    #Creating a window
    win = GraphWin("Magic Square",500,500)
    win.setCoords(0,0,100,100)

    #Text messages
    textmessage = Text(Point(50,96), "Please enter the square size and click the Draw button.")
    textmessage.setSize(12)
    textmessage.draw(win)
    
    textmessage_square_size = Text(Point(7,95),"Square Size:")
    textmessage_square_size.setSize(11)
    textmessage_square_size.draw(win)

    #Button for Draw
    button_draw = Rectangle(Point(4,2), Point(16,8))
    button_draw.draw(win)
    draw_message = Text(Point(10,5), "Draw")
    draw_message.draw(win)
    
    #Button for Exit
    button_exit = Rectangle(Point(18,2), Point(30,8))
    button_exit.draw(win)
    exit_message = Text(Point(24,5),"Exit")
    exit_message.draw(win)
    
    #Entry from user
    entry = Entry(Point(17,95),4)
    entry.draw(win)

    
    once = True
    line_list = []
    nums=[]
    square_size = 0
    
    while(once):
        
        #Getting a mouse click
        click = win.getMouse()  
        
        #If clicked on the Exit Button, break program
        if click.x >= 18 and click.x <= 30 and click.y >= 2 and click.y <= 8:
            break

        #If clicked on the Draw Button, then redraw everything
        if click.x >= 4 and click.x <= 16 and click.y >= 2 and click.y <= 8:

            #Making sure that user inputs a valid square size
            n = entry.getText()
            try:
                answer = eval(n)
            except:
                textmessage.setText("Please enter the square size and click the Draw button.")
                continue
            if (answer >=1 or answer<=49) and (answer %2==1):
                pass
            else:
                textmessage.setText("Please enter a positive odd number that is less than 49.")
                continue

            #Remove all grid and numbers
            for k in nums:
                txtLst[k].undraw()

            for line in line_list:
                line.undraw()

            #Calculating width of grid and cell width
            line_list = []
            square_size = answer
            cell_width = 80//(square_size)
            width = cell_width * (square_size)
            
            #Defining top left and right bottom
            top_left = Point(10,90)
            right_bottom = Point(top_left.x + width, top_left.y + width)

            #Draw Grid
            for i in range(int(square_size)+1):
                points_vertical = Point(top_left.x, top_left.y - cell_width*i)
                line_list.append(Line(Point(points_vertical.x,points_vertical.y), Point(points_vertical.x + width, points_vertical.y)))
                points_horizontal = Point(top_left.x + cell_width*i, top_left.y)
                line_list.append(Line(Point(points_horizontal.x, points_horizontal.y), Point(points_horizontal.x, points_horizontal.y - width)))              
            for line in line_list:
                line.draw(win)
                                  
            #Text Message for clicking the block for placing 1
            textmessage.setText("Please click the block for placing 1.")

            continue
        
        #Inside possible grid
        if click.x >= 10 and click.x <= 90 and click.y >= 10 and click.y <= 90:
            if square_size == 0:
                continue
        
            #Implementing algorithm for putting numbers in right place
            cx = -1
            cy = -1
            for cg in range(int(square_size)+1):
                if click.x > 10 + cell_width * (cg-1) and click.x <= 10 + cell_width *cg:
                    cx = cg - 1
            for rg in range(int(square_size)+1):
                if click.y < 90 - cell_width * (rg-1) and click.y >= 90- cell_width *rg:
                    cy = rg - 1
            if cx == -1 or cy == -1:
                continue

            #Text Message for waiting
            textmessage.setText("Please wait....")
        
            #Creating one empty list
            filled = []
            for m in range(int(square_size)):
                filled.append ([0]*(square_size))      

            # Creating one dimensional list
            txtLst = []
            txtLst.append(Text(Point(1,1), str(0)))
           
            for i in range(1,(int(square_size)**2)+1):
                txtLst.append(Text(Point(5,85), str(i)))
                txtLst[i].setTextColor("blue")
                txtLst[i].setSize(26)

            for k in range(1,(int(square_size)**2)+1):
                filled[cx][cy] = 1
                x_coord, y_coord = calculateCoordinates (top_left,right_bottom,cell_width,cx+1,cy+1)
                
                txtLst[k].draw(win)
                nums.append(k)
                move(txtLst[k],5,85,x_coord,y_coord)
                
                oldx = cx
                oldy = cy
                cx = cx + 1
                cy = cy + 1 
                if cx == int(square_size):
                    cx = 0
                if cy == int(square_size):
                    cy = 0 
                                       
                if filled [cx][cy] == 1:
                    cx = oldx
                    cy = oldy
                    cy = cy - 1
                    if cy == - 1:
                        cy = int(square_size) - 1

            textmessage.setText("Please enter the square size and click the Draw button.")
                        
            continue
                        
    
    win.close()
    
main()