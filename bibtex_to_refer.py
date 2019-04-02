# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:56:33 2019

@author: bdatko
"""
# Parse agruments from command line
import argparse

import bibtexparser

def main():
    # Purpose transform BibTex database into a bib refer database
    
    parser = argparse.ArgumentParser()
    
    # Set up required arguments
    parser.add_argument('filename', type=str)
    
    args = parser.parse_args()
    
    # get the bib database
    with open(args.filename, encoding='utf8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        
    
    
    # initialize the dict
    # create the keys
    keys = ['%A', '%B', '%C', 
            '%D', '%E', '%G',
            '%I', '%J', '%K', 
            '%L', '%N', '%O',
            '%P', '%Q', '%R', 
            '%S', '%T', '%V', '%X']
    
    refer_entry = dict.fromkeys(keys)
    
    
    # create the switch case for refer
    def author():
        refer_entry['%A'] = bib_entry.get('author')
            
    def booktitle():
        refer_entry['%B'] = bib_entry.get('title')
            
    def address():
        refer_entry['%C'] = bib_entry.get('address')
            
    def year():
        date = bib_entry.get('year')
            
        if "month" in bib_entry:
            date = bib_entry.get('month') + " " + date
            refer_entry['%D'] = date
        else:
            refer_entry['%D'] = date
            
    def editor():
        refer_entry['%C'] = bib_entry.get('editor')
            
    def publisher():
        refer_entry['%I'] = bib_entry.get('publisher')
            
    def journal():
        refer_entry['%J'] = bib_entry.get('journal')
            
    def keyword():
        refer_entry['%K'] = bib_entry.get('ID')
            
    def label():
        refer_entry['%L'] = bib_entry.get('ENTRYTYPE')
            
    def number():
        refer_entry['%N'] = bib_entry.get('number')
        
    def other():
        refer_entry['%O'] = bib_entry.get('howpublished')
            
    def pages():
        refer_entry['%P'] = bib_entry.get('pages')
            
    def note():
        refer_entry['%Q'] = bib_entry.get('note')
            
    def report_number():
        refer_entry['%R'] = bib_entry.get('number')
            
    def series():
        refer_entry['%S'] = bib_entry.get('series')
            
    def title():
        refer_entry['%T'] = bib_entry.get('title')
            
    def volume():
        refer_entry['%V'] = bib_entry.get('volume')
            
    def annote():
        refer_entry['%X'] = bib_entry.get('annote')
            
    # map the inputs to the function blocks
    refer = {'author' : author,
               'booktitle' : booktitle,
               'address' : address,
               'year' : year,
               'editor' : editor,
               'publisher' : publisher,
               'journal' : journal,
               'keyword' : keyword,
               'label' : label,
               'number' : number,
               'pages' : pages,
               'note' : note,
               'howpublished' : other,
               'report_number' : report_number,
               'series' : series,
               'title' : title,
               'volume' : volume,
               'annote' : annote,
               }

    # parse the bib entry into the new dict
    # goal is to loop over the newly made dict and print the bib file

    for bib_entry in bib_database.entries:
        
        refer['keyword']()
        refer['label']()
        
        for field_type in bib_entry:
            if field_type in refer:
                refer[field_type]()
                
        for key,value in refer_entry.items():
            
            if value is not None:
                
                if key == '%A':
                    
                    value = value.split(sep='and ')
                    
                    for author in value:
                        print("{0} {1}".format(key, author))
                else:
                    print("{0} {1}".format(key, value))
                
        print("\n")
        refer_entry = dict.fromkeys(keys)
        

if __name__ == '__main__':
    main()
    
