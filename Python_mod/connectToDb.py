##importing the pymongo packages to get the corresponding connection with the db
import pymongo

import sys
import re
regex = re.compile('Massive')

##rstats = posts.find_one({"text":regex})
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


client = pymongo.MongoClient("localhost", 27017)
# TwitterDb is the name of the Db created other than the default db test
db=client.TwitterDb

print("database name is "+db.name)
# here the TwitterData is the name of the collection created for storing the twitter data in the cursor to get all the records
cursor = db.TwitterData.find_one({"text":regex})
print (cursor)
##cursor = db.TwitterData.find_one({"text":regex})
#iterating the cursor to print the values of the dcument in the collection
#for document in cursor:
    ##textTObEAnalyzed=str(document).translate(non_bmp_map)
    
   ## print(str(document.find_one({"text":regex})).translate(non_bmp_map))
    #print(document.find_one({"text":regex}))
        ## str(x1).trdictanslate(non_bmp_map)
        
    

    
       
        
