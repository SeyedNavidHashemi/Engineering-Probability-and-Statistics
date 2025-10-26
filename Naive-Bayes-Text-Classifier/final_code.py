import numpy as np
import pandas as pd 
from math import log
from hazm import Stemmer
from hazm import WordTokenizer
tokenizer = WordTokenizer()
epsilon = 0.5
num_of_cat = 6
correct_answers = 0
wrong_answers = 0


#this part is about unusable characters and stop words
unusable_char = "؟\"!.۰،,?()-؛:»«123456789۱۲۳۴۵۶۷۸۹\\//\r"
df = pd.read_csv('sw.csv')
stop_words = df[df.columns[0]].tolist()


#functions
#removing unuseful characters
def remove_special_characters(phrase):
    for letter in unusable_char:
        index = phrase.find(letter)
        if index != -1:
            phrase = phrase.replace(phrase[index], "")
    return phrase

#this function calculates numbers of each testing book and final probability
def calculate_probability(book_info, list_of_sums):
    base_dict = {"c1" : 0, "c2" : 0, "c3" : 0, "c4" : 0, "c5" : 0, "c6" : 0}
    categ = book_info["categorie_"]
    del(book_info["categorie_"])
    for word in book_info:
        try:
            zero_in_bow = 0
            sotun = bag_of_word_df_train[word]
            for index_row in range(1, num_of_cat + 1):
                # print(index_row)
                cat_name = "c" + str(index_row)
                #this part is for simple state
                if sotun[index_row - 1] == 0:
                   zero_in_bow = 1
                if zero_in_bow == 1:
                    break   
                base_dict[cat_name] += ((book_info[word] * log(sotun[index_row - 1] / list_of_sums[index_row - 1], 2)))
                # print(base_dict[cat_name])
        except:
            pass
    
    max_cat = max(base_dict, key = base_dict.get)
    check_if_guess_is_correct(categ, max_cat) 

def check_if_guess_is_correct(cat, max_cat):
    global correct_answers
    global wrong_answers
    original_answer = "c" + str(categories[cat])
    if max_cat == original_answer:
        correct_answers += 1
    else:
        wrong_answers += 1
    
#this variables are nub=mber of each categori for calculating prior probability
num_cat1, num_cat2, num_cat3, num_cat4, num_cat5, num_cat6 = 0, 0, 0, 0, 0, 0

#calculate number of each categorie in boook.train
def categorie_number_calculator(categorie):
    if categorie == "مدیریت و کسب و کار":
        global num_cat1
        num_cat1 += 1
    elif categorie == "رمان":
        global num_cat2
        num_cat2 += 1
    elif categorie == "کلیات اسلام":
        global num_cat3
        num_cat3 += 1
    elif categorie == "داستان کودک و نوجوانان":
        global num_cat4
        num_cat4 += 1
    elif categorie == "جامعه‌شناسی":
        global num_cat5
        num_cat5 += 1
    else:
        global num_cat6
        num_cat6 += 1

#it find categori and sends to update_..._second function
def update_cat_bag_of_words_first(list_of_words, cat_code):
    if cat_code == 1:
        update_cat_bag_of_words_second(list_of_words, train_cat1)
    elif cat_code == 2:
        update_cat_bag_of_words_second(list_of_words, train_cat2)
    elif cat_code == 3:
        update_cat_bag_of_words_second(list_of_words, train_cat3)
    elif cat_code == 4:
        update_cat_bag_of_words_second(list_of_words, train_cat4)
    elif cat_code == 5:
        update_cat_bag_of_words_second(list_of_words, train_cat5)
    else:
        update_cat_bag_of_words_second(list_of_words, train_cat6)

def update_cat_bag_of_words_second(list_of_words, cat_dict):
        
    update_all_words_train(list_of_words)

    for word in list_of_words:
        if word in cat_dict:
            cat_dict[word] += 1 
        else:
            cat_dict[word] = 1

def update_all_words_train(list_of_words):
    for word in list_of_words:
        if word in train_all_words:
            train_all_words[word] += 1 
        else:
            train_all_words[word] = 1
#it make dictionary of words and their repeats
def make_book_words_dict(list_of_words, categorie):
    words = dict()
    words["categorie_"] = categorie
    for word in list_of_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

#reading csv file by pandas library:
#BOOKS_TRAIN.CSV:
books_train_data = pd.read_csv("books_train.csv")  
train_titles = books_train_data['title']
train_desc = books_train_data['description']
#BOOKS_TEST.CSV:
books_test_data = pd.read_csv("books_test.csv")
test_titles = books_test_data['title']
test_desc = books_test_data['description']

#removing unusful characters from files:
#BOOKS_TRAIN.CSV:
for i in range(0, len(train_titles)):
    train_titles[i] = remove_special_characters(train_titles[i])
for j in range(0, len(train_desc)):
    train_desc[j] = remove_special_characters(train_desc[j])
#BOOKS_TEST.CSV:
for i in range(0, len(test_titles)):
    test_titles[i] = remove_special_characters(test_titles[i])
for j in range(0, len(test_desc)):
    test_desc[j] = remove_special_characters(test_desc[j])

categories = {'مدیریت و کسب و کار' : 1, 'رمان': 2, 'کلیات اسلام' : 3,
            'داستان کودک و نوجوانان' : 4, 'جامعه‌شناسی' : 5, 'داستان کوتاه' : 6}

#dictionaries related to books.train.csv
train_cat1 = dict()
train_cat2 = dict()
train_cat3 = dict()
train_cat4 = dict()
train_cat5 = dict()
train_cat6 = dict()
train_all_words = dict() 

for i in range(0, len(books_train_data)):
    sub = "train"
    categori = books_train_data.iloc[i][2]
    desc = tokenizer.tokenize(books_train_data.iloc[i][1])
    ti = tokenizer.tokenize(books_train_data.iloc[i][0])
    #this part removes stop words from title and discription
    for stop_w in stop_words:
        for w in desc:
            if w == stop_w:
                desc.remove(w)
    for stop_w in stop_words:
        if stop_w in ti:
                ti.remove(stop_w)
    #this part rishe yabi mokinad
    new_desc = list()
    for word in desc:
        rishe = Stemmer().stem(word)
        new_desc.append(rishe)
    new_ti = list()
    for word in ti:
        rishe = Stemmer().stem(word)
        new_ti.append(rishe)
    categorie_number_calculator(categori)
    update_cat_bag_of_words_first(new_desc, categories[categori])
    update_cat_bag_of_words_first(new_ti, categories[categori])

list_of_all_dic_of_test_words = list()

for k in range(0, len(books_test_data)):
    subj = "test"
    cat = books_test_data.iloc[k][2]
    des = remove_special_characters(books_test_data.iloc[k][1])
    des = tokenizer.tokenize(des)
    tit = remove_special_characters(books_test_data.iloc[k][0])
    tit = tokenizer.tokenize(tit)
    #this part removes stop words from title and discription
    for stop_w in stop_words:
        for w in des:
            if w == stop_w:
                des.remove(w)
    for stop_w in stop_words:
        if stop_w in tit:
            tit.remove(stop_w)
    all_words = des + tit
    # rishe yabi
    new_all_words = list()
    for word in all_words:
        rishe = Stemmer().stem(word)
        new_all_words.append(rishe)
    new_book_info_dictionary = make_book_words_dict(new_all_words, cat)
    list_of_all_dic_of_test_words.append(new_book_info_dictionary)
   
#bag_of_words_of_train
list_of_dict_of_train = [train_cat1, train_cat2, train_cat3, train_cat4, train_cat5, train_cat6]
bag_of_word_df_train = pd.DataFrame.from_records(list_of_dict_of_train,index=['1', '2', '3', '4', '5', '6'])
bag_of_word_df_train += epsilon
bag_of_word_df_train = bag_of_word_df_train.fillna(epsilon)
bag_of_word_df_train["all_sum"] = bag_of_word_df_train.sum(axis=1)
list_of_sums = bag_of_word_df_train["all_sum"].to_list()


#calculating probability
for book_dict in list_of_all_dic_of_test_words:
    calculate_probability(book_dict, list_of_sums)

#print_result
print("Resolution: ", correct_answers, "/", len(list_of_all_dic_of_test_words))