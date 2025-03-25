from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text=request.GET['fulltext']
    word_list=entered_text.split()
    word_dictionary={}
    allword=len(word_list)
    text_count=len(entered_text)
    only_text=text_count
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    most_freq_cnt=max(word_dictionary.values())
    most_freq=[]

    for word, count in word_dictionary.items(): 
        if count == most_freq_cnt: 
            most_freq.append(word)  

    for space in entered_text:
        if space==" ":
            only_text-=1
    
   
    return render(request, 'result.html', {'onlytextcnt':only_text, 'allword': allword, 'alltext': entered_text, 
                                           'dictionary':word_dictionary.items(), 'textcnt':text_count,
                                           'most_count':most_freq_cnt, 'most':most_freq})

def hello(request):
    user_name=request.GET['name']
    return render(request, 'hello.html', {'name':user_name})