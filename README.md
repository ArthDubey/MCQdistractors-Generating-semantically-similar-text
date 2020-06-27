# Generating semantially similar text 
This project aims to generate semantically and structurally similar text while keeping the context of the statement. 
- Major use of this could be generating 2 or more options for a given question and solution of a Multiple choice question. 
- Another major use could be suggesting alternative statements for a typed statement in an email or essay.



## Creation of Vocabulary

The following steps were followed in order to create the Vocabulary-
1. All of the words from the train.csv file and test.csv file along with their number of occurances were saved in pickle format.
2. As this vocabulary may not have been extensive enough for us to get the words we needed. For example

   _In example 149 in the submitted 'answer.csv' you can find, the actual answer is - 'The dummies books will continue to be     popular' and the generated distractors are - 'The crosswords books will continue to be popular.' and 
   'The dummies books will cease to be popular .'_

   As the words 'cease' and 'crosswords' (which were essential in creating distractors) may not have been on the vocabulary so   some essential extra words of English were needed.

3. So the following Corpus was additionally used to expand the vocabulary.

   Source - http://www.nltk.org/nltk_data/ (28th entry)

   Web Text Corpus [ download | source ]
   id: webtext; size: 646297; author: ; copyright: ; license: ;

4. Thus the Voacabulary used in this project was created.


## Training word embedding model for Vector space representation of the words

1. After the procured text was created to be used as Corpus, all the unnecessary entries ('~!@#$%^&*()+}{|":') were filtered out.
2. All of the existing words were lemmatized so that the word2vec model would be able to extract more meaning from the corpus, since words like 'study' and 'studying' would mean the same thing.
3. Stop words were removed from the corpus.
4. Now after the procurement was complete vsmlib was used in order to train the word2vec model with the following hyperparameters (To find more, please refer to 'AdvancedTrain.py') -
   {
      "dimensions": 25,
      "epoch": 5,
      "negative_size": 2,
      "model": "cbow",
      "out_type": "ns",
      "subword": "none",
      "window": 2
}
5. The trained model was now stored in npy format along with the metadata.


## Approach to generate the text

The approach to generate the text is-

For every iteration of Test.csv-
   - The actual solution is tokenized by the help of NLTK.
   - All of the nouns and the verbs are extracted (with nltk.pos_tag) and stored in set.
   - The vector representation of the nouns and verbs are then found.
   - For the first distractor, Noun in the subject is swapped with the word with minimum Euclidean distance from it in the vector space representation. 
   - For the second distractor, Verb in the subject is swapped with the word with minimum Euclidean distance from it in the vector space representation. 
   - If there is no noun or there is no verb in the subject of the sentence, Then any noun or verb found in the sentence are used.
   - If the vector space representation comes up with a word which is very similar to the existing word, then nltk.corpus.wordnet.synsets are iterated over to find the best fit.
   - The solution is stored in answer.csv


## Results
The results of this approach were not perfect but quite better than all the other alternatives tried. In most other alternatives, either contextual integrity of the solution was compromised or results were gramatically nonsensical.

Some of the noteworthy examples for the results are

| Question        | Solution           | Distractors  |
| ------------- |:-------------:| -----:|
| What is special about Caleb Street 's Inn ? |It has a golf course for guest| 'It has a softball course for guest','It had football court for guests' |
|What happened to them a few minute later ? | their car nearly hit another car | 'their sailboat nearly hit another sailboat','Their car nearly stopped other car'|
| Which of the following is right ?| Jim has many English books . |'Jim has many French books .','Jim had many English books'|


## Authors

* **Arth Dubey** 

