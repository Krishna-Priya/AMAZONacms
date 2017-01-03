


a= [[0,0,0,0,1],[0,0,0,1,1],[1,1,1,0,'d'],[0,'d',0,0,0],[0,0,0,0,0]]

width=height=5
x,y=2,0
for x_ in range(max(0,x-4),min(width,x+8)):
  for y_ in range(max(0,y-4),min(height,y+8)):
    if (x,y)==(x_,y_):
	if (y_ == 0 or y_ == width-1) :
		if(a[x_+1][y_] or a[x_-1][y_] or a[x_][y_+1] or a[x_-1][y_+1] or a[x_+1][y_+1]) == 'd':
			print 'd'
	#elif (x_ == 0 or x_ == 4) :
	# 	if(               )
#    print x_ ,y_
#   if a[x_][y_] == 'd':
#	 print "driver" ,a[x_][y_] ,"is at" ,x_,y_

