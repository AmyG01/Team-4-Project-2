# Team-4-Project-2
Python Functions which calculate Metrics using Eskom Data

## Technologies
*Python 3.7
 > Pandas Package Version 1.0
 > Numpy Package Version 1.18
 *IDE
 >VS Code
 >Jupyter notebook

## Prerequisites
*Windows OS
*Python Integrated Development Environment ( Jupyter, VSCode , Note++ etc )

## Installing

1. Initiate a Command Window ( Git Bash is recommended )
 
2. Issue the command below to install your package from GitHub.
   >pip install git+https://github.com/AmyG01/Team-4-Project-2.git

## Usage

On the IDE window import the Eskom Metrics Package as illustrated below

>>> import EskomMetric as em

#### Metric Dictionary

>>> Call - em.dictionary_of_metrics() | Arg : List of intergers or floats

#### Five Number Summary

>>> Call - em.five_num_summary() | Arg : Unordered list of intergers or floats

#### Date Parser

>>> Call - em.date_parser() | Arg : List of strings where each element(date)
        				                  is in the format 'yyyy-mm-dd' and 'hh:mm:ss'

#### Municipality & Hashtag Detector

>>> Call - em.extract_municipality_hashtags() | Arg : A pandas dataframe as input

#### Number of Tweets per Day

>>> Call - em.number_of_tweets_per_day() | Arg : A pandas dataframe as input

#### Word Splitter

>>> Call - em.word_splitter() | Arg : A pandas dataframe as input

#### Stop Words

>>> Call - em.stop_words_remover() | Arg : A pandas dataframe as input

## Versioning
Git version control was used for this project.

## Contributing
For any contributions you may have for this project, kindly contact any one of the team members via email.


## Authors

1.Refentse Motlogelwa
2.Philani Mkhize
3.Lizwi Khanyile
4.Gugu Mtonjeni
5.Sibonelo Malakiya Jr

## Licenses

This project is licensed under the MIT License

## Acknowledgments

Stackoverflow
