import csv
class MazeGen:
    def __init__(self, ifile):
        self.ifile = ifile
        self.dict ={}
        file1 = open(self.ifile, 'r')
        self.Lines = file1.readlines()
        self.parse()

    def parse(self):
        for line in self.Lines:
            line = line.strip()
            #split by comma, concatenate first to elements as key, rest of line as value for dict
            line = line.split(',')
            key = line[0] +','+ line[1]
            key=key.strip('"'"'")
            val = line[2:]
            #compute binary wall values
            for i in range(0,len(val)):
                if val[i] <= str(0.25):
                    val[i]=0
                else:
                    val[i]=1
            self.dict[key] = val

    
    def createCSV(self):
        #outputs csv 'mymazefile'
        with open('mymazefile.csv', 'w', newline='') as f: 
            w = csv.writer(f)
            #write header
            w.writerow(["  cell  ","E","W","N","S"])
            #call key/val pairs in order and write to csv
            for i in range(1,5):
                for j in range(1,5):
                    s = "("+str(j)+", "+str(i)+")"
                    w.writerow([s]+self.dict[s])

