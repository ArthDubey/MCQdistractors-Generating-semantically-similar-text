# MCQdistractors-Generating-semantially-similar-text || Submission for ValueLabs
This project aims to generate semantially and structurally similar text while keeping the context of the statement. Major use of this could be generating 2 or more distractors given the question and solution of a Multiple choice question.



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
4. Now after the procurement was complete vsmlib was used in order to train the word2vec model with the following hyperparameters (To find more refer to 'AdvancedTrain.py') -
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
   1. The actual solution is tokenized by the help of NLTK.
   2. All of the nouns and the verbs are extracted and stored in set.
   3. The vector representation of the nouns and verbs are then found.
   4. For the first distractor, Noun in the subject is swapped with the word with minimum Euclidean distance from it in the vector space representation. 
   5. For the first distractor, Verb in the subject is swapped with the word with minimum Euclidean distance from it in the vector space representation. 
   6. If there is no noun or there is no verb in the subject of the sentence, Then any noun or verb found in the sentence are used.
   7. If the vector space representation comes up with a word which is very similar to the existing word, then nltk.corpus.wordnet.synsets are iterated over to find the best fit.
   8. The solution is stored in answer.csv




### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
