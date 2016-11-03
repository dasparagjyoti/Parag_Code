__author__= "paragjyoti"




'''REVISIONS !!! '''







from extra import *

#Usage
#parameter 1: Name of the problem file
#parameter 2: EPSILON value
#parameter 3: Minimum confidence


if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);


    parser = argparse.ArgumentParser()
    parser.add_argument(dest='F',help="Name of the problem file")
    parser.add_argument(dest='epsilon',help="Epsilon value",type=float)
    parser.add_argument(dest='delta',help="Minimum Confidence",type=float)
    args, unknown = parser.parse_known_args() #using parse_known_args rather than parse_args enables the use of ArgumentParser in code within the scope of if __name__ 

    F = args.F
    epsilon = args.epsilon
    delta = args.delta

    


    counter=0
    c=[]
    pivot=2*compute_threshold(epsilon)
    t=computeiter_count(delta)  

    while (counter<t) :
        c=ApproxMcCore(F,pivot)#To be define #Pisot koribo lagibo
        counter = counter+1
        if c!=1:
            AddToList(C,c)#To be define
    final_count=find_median(c) 
    X=final_count
          
           
