
# Extracting Comments from Worldnews SubREddit using Pushshift API
import json
from IPython.display import display
import pandas as pd
import time

import requests
from urllib.parse import urljoin
url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=worldnews&after=1533081601&before=1535587201&sort=asc&fields=body,permalink,score&size=100'
request = requests.get(url)
print(type(request.content))
json = request.json()       #convert request contents from bytes to json
comments = json['data']     # Store all 'values' in the list variable -> comments
display(comments)

print(len(comments))
#Observation API limits results to 100 comments per request

def pushcall(after, before):
    #Function to call multiple arguments into several parameters for the Pushshift api
    mysort = ['asc', 'desc']
    df = pd.DataFrame()
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=worldnews&fields=body,score,permalink&size=100'
    for order in mysort:
        resp = requests.get(url, {'sort':order, 'after':after,'before':before})
        json = resp.json()
        comments= json['data']
        df1 = pd.DataFrame(comments, columns=['body', 'score', 'permalink'])
        df = pd.concat([df,df1])
        time.sleep(0.4) # prevents connection from timeout or ending 5 milliseconds
    return df

after = [
    1540425605, 1539907205, 1539388805, 1538870405, 1538352005,
    1537833605, 1537315205, 1536796805, 1536278405, 1535760005,
    1535155205, 1534636805, 1534118405, 1533600005, 1533081605,
    1532476805, 1531958405, 1531440005, 1530921605, 1530403205,
    1529884805, 1529366405, 1528848005, 1528329605, 1527811205
    ]
before = [
    1540857605, 1540339205, 1539820805, 1539302405, 1538784005,
    1538265605, 1537747205, 1537228805, 1536710405, 1536192005,
    1535587205, 1535068805, 1534550405, 1534032005, 1533513605,
    1532908805, 1532390405, 1531872005, 1531353605, 1530835205,
    1530316805, 1529798405, 1529280005, 1528761605, 1528243205
    ]


dfmain = pd.DataFrame()     #initiate decoy dataframe
for x,y in zip(after, before):
    pushcall(x,y)           #function call
    temp = pushcall(x,y)    #store data fram in variable 'temp'
    dfmain = pd.concat([temp, dfmain])    #concat on axis=0 : i.e rows

display(dfmain)

# Some Data Cleaning
"""
    ## The next step is to clean the data i.e.
    (i) Remove all records with [deleted], [removed], Weblinks(https, www)
    (ii) remove all records with character lenght greater than(>=) 1000 and less than (<=) 70
"""

df = dfmain[~(dfmain['body'] == "[removed]")]               # '~' is the operator for 'isnot' in pandas
df = df[~(df['body'] == "[deleted]")]                

#The syntax directly below helps remove all http links
df['body'] = df['body'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True).replace(r'http:\S+', '', regex=True) 

df= df[df.body.apply(lambda x: len(str(x))<=1000)]         # Remove records with character length > 1000
df= df[df.body.apply(lambda x: len(str(x))>=50)]            # Remove records with character lenght <70
display(df.body.head(5))
display(df.info)


# Extracting topic title from permalink
display(df['permalink'].head(10))

df.permalink =df['permalink'].apply(lambda x: x.split('/')).apply(lambda x: x[5].replace('_', ' '))
display(df['permalink'].head(10))


#Save final Dataset into a csv
display(df)
#df.to_csv("redcom_1.csv", index=False)  

