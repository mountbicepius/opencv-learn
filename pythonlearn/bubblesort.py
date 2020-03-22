def sort(arg):
        mSwaps = True
        while mSwaps:
            mSwaps = False
            for value in range(len(arg)-1):
                if arg[value]> arg[value+1]:
                    mSwaps = True
                    temp = arg[value]
                    arg[value]= arg[value+1]
                    arg[value+1]=temp
        return arg
def testSorting():
        arg = [12,2,13,18,8,7,4,1]
        sorted= sort(arg)
        print(sorted)
        pass
