import pandas as pd
import nltk
from nltk.corpus import wordnet
import vsmlib


my_vsm = vsmlib.model.load_from_dir("trainedData")
my_vsm.normalize()


def utop(sy):
    sy=str(sy)
    is_noun = lambda pos: pos[:2] == 'NN'
    is_verb=lambda x:x[:2] == 'VB'
    tokenized = nltk.word_tokenize(sy)
    nouns=[]
    verbs=[]
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    if nouns==[]:
        q1= sy
    if verbs==[]:
        q2= sy
    clip=sy
    snouns=set(nouns)
    sverbs=set(verbs)
    for i in tokenized:
        if i in snouns:
            try:
                we=wordnet.synsets(i)[0].lemmas()[0].name()
                ind=0
                while i.lower()==we.lower():
                    ind+=1
                    we=wordnet.synsets(i)[ind].lemmas()[0].name()
                q1=sy.replace(i,we)
            except:
                q1=sy
                continue
            break
    for i in tokenized:
        if i in sverbs:
            try:
                we=wordnet.synsets(i)[0].lemmas()[0].name()
                q2=clip.replace(i,we)
            except:
                q2=clip
                continue
            break
    qq=q1+'''", "'''+q2+'''", "'''+sy
    return qq


def vtop(sy):
    sy=str(sy)
    is_noun = lambda pos: pos[:2] == 'NN'
    is_verb=lambda x:x[:2] == 'VB'
    tokenized = nltk.word_tokenize(sy)
    nouns=[]
    verbs=[]
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    if nouns==[]:
        q1= sy
    if verbs==[]:
        q2= sy
    clip=sy
    snouns=set(nouns)
    sverbs=set(verbs)

    for i in tokenized:
        if i in snouns:
            try:
                we=my_vsm.get_most_similar_words(i, cnt=2)[1][0]
                ind=0
                if we=='¥':
                    we=wordnet.synsets(i)[ind].lemmas()[0].name()
                
                
                while i.lower()==we.lower():
                    ind+=1
                    we=wordnet.synsets(i)[ind].lemmas()[0].name()
                q1=sy.replace(i,we)
            except:
                q1=sy
                continue
            break
    for i in tokenized:
        if i in sverbs:
            try:
                we=my_vsm.get_most_similar_words(i, cnt=2)[1][0]
                ind=0
                if we=='¥':
                    we=wordnet.synsets(i)[ind].lemmas()[0].name()
                
                while i.lower()==we.lower():
                    ind+=1
                    we=wordnet.synsets(i)[ind].lemmas()[0].name()
                q2=clip.replace(i,we)
            except:
                q2=clip
                continue
            break

    
    qq="'"+q1+"""', '"""+q2+"'"
    return qq


df=pd.read_csv("Test.csv")

hih=list(df["answer_text"])
#print(hih[:10])
l=[vtop(i) for i in hih]
realdf=pd.DataFrame(l,columns=["distractor"])
ansdf=[df,realdf]
ans=pd.concat(ansdf,axis=1)

ans.to_csv("answer.csv",index=False)



