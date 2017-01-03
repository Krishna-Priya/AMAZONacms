passenger = "passenger"
driver = "driver"
role =input("Enter your role(passenger or driver)")
def driver_op(m,n):

        print("Route1")
        Route1 = [1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0]
        matrix = [ Route1[i:i+5] for i in range(0,len(Route1),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
            print l
        print
        print("Route2")

        Route2 = [0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
        matrix = [ Route2[i:i+5] for i in range(0,len(Route2),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
          print l
        print
        print("Route3")

        Route3 = [0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0]
        matrix = [ Route3[i:i+5] for i in range(0,len(Route3),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
                 print l
if(role == passenger):
	print("please select any route ")
	print("Route1")
	Route1 = [1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0] 
	matrix = [ Route1[i:i+5] for i in range(0,len(Route1),5) ]
	for l in matrix:
	      print l
	print
	print("Route2")
	Route2 = [0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0] 
	matrix = [ Route2[i:i+5] for i in range(0,len(Route2),5) ]
	for l in matrix:
    		 print l
	print
	print("Route3")
	Route3 = [0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0]   
	matrix = [ Route3[i:i+5] for i in range(0,len(Route3),5) ]
	for l in matrix:
	     print l
	route  =  int(input("Enter the route selected:"))
	#print(route)
elif(role == driver):
#	(m,n) = input("Enter the coordinate you belong to:")
	m = int(input("enter your x- co-ordinate"))
	n = int(input("enter your y - co-ordinate"))
	driver_op(m,n)


def driver_op(m,n):

        print("Route1")
        Route1 = [1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0]
        matrix = [ Route1[i:i+5] for i in range(0,len(Route1),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
            print l
        print
        print("Route2")

        Route2 = [0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
        matrix = [ Route2[i:i+5] for i in range(0,len(Route2),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
          print l
        print
        print("Route3")

        Route3 = [0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0]
        matrix = [ Route3[i:i+5] for i in range(0,len(Route3),5) ]
        matrix[m][n] = 'd'
        for l in matrix:
                 print l
	
def get_adjacent_cells( self, x_coord, y_coord ):
    result = {}
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if (x,y) in grid.cells:
            result[(x,y)] = grid.cells[(x,y)]

