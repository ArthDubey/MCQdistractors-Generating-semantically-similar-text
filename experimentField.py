import nltk
import pandas as pd
def giver(sy):
    sy=str(sy)
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(sy)
    nouns=[]
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    if nouns==[]:
        return sy
    qq=" ".join(nouns[:-1])+''', '''+" ".join(nouns[1:])
    return qq
hih=['The lack of career -- based courses in US high schools', 'the sun is out at night', 'have to get confirmed at least twice', 'nobody made room for him in the water .', 'There are twelve countries in the World Wildlife Fund .', 'it may make it difficult for customers to recover their data', 'how Billy made blueberry juice with his uncle', "The snail 's teeth ca n't be worn out ..", 'Eat the food your host family gives you .', 'how to make a meaningful DIY card']
l=[giver(i) for i in hih]

realdf=pd.DataFrame(l,columns=["distractor"])
print(realdf)
# ans=pd.concat(ansdf,axis=1)

# ans.to_csv("answer.csv",index=False)