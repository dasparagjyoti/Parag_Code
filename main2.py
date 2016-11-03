from extra import *

#Usage
#parameter 1: Name of the problem file
#parameter 2: PIVOT value


if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);


    parser = argparse.ArgumentParser()
    parser.add_argument(dest='F',help="Name of the problem file")
    parser.add_argument(dest='pivot',help="Pivot value",type=float)
    args, unknown = parser.parse_known_args() #using parse_known_args ran parse_args enables the use of ArgumentParser in code within the scope of if __name__ 

    F = args.F
    pivot = args.pivot



    S=boundsat(F,pivot+1)#extra2 t likh function define
    if
       (|S|<=pivot)
        Y=|S|
    else
        l=|log|#extra2 t expression write
    
