
from generator import LCG, SCG
from point import Point
import timeit


def test(randnumbers):
    
    start = timeit.default_timer()
    #print(randnumbers)
    points=[]
    for i in range(int(len(randnumbers)/2)):
        points.append([randnumbers[2*i],randnumbers[2*i+1]])
    #print(points)     
        
    point_distance_list=[]
    for p in points:
        #print(p)
        get_point=Point(p[0],p[1])
        point_distance_list.append(get_point.distance())
        
    #print(point_distance_list)
    
    #theoretical result of this ratio
    theory_ratio=0.78539816339
    print('theoretical result of this ratio',theory_ratio)
    number_of_points=len(points)
    print('number_of_points',number_of_points)
    number_of_points_within_circle=0
    for x in point_distance_list:
        if x<=1:
            number_of_points_within_circle=number_of_points_within_circle+1
            
    print('number_of_points_within_circle',number_of_points_within_circle)
    #calculating ratio of points       
    ratio_points_within_cicle=number_of_points_within_circle/number_of_points
    print('ratio_points_within_cicle',ratio_points_within_cicle)
    stop = timeit.default_timer()
    print('Time taken ',stop-start) 
    
if __name__ == '__main__':       
    #Creating points with random numbers
    LCGgeneratorpoints=LCG(1,1103515245,12345,2**32)
    RandomNumberList=LCGgeneratorpoints.numberSequence(20000000)
    test(RandomNumberList)
    
    SCGgeneratorpoints=SCG(2,2**32)  
    RandomNumberList1=SCGgeneratorpoints.getSequence(20000000)
    test(RandomNumberList1)
