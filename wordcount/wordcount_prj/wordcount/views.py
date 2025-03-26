from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def word_count(request):
    return render(request,'word_count.html')

def hello(request):
    name=request.GET['name']
    return render(request,'hello.html',{'name':name})

def result(request):
    entered_text=request.GET['fulltext']
    all_word=len(entered_text)
    all_word_nspace = len(entered_text.replace(" ", ""))
    word_list=entered_text.split()
    total_count=len(word_list)
    max_count=0
    common_word=[]
    word_dictionary={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    for word, count in word_dictionary.items():
        if count>max_count:
            max_count=count
            common_word=[word]
        elif count==max_count:
            common_word.append(word)

    return render(request,'result.html',{'alltext': entered_text,'dictionary':word_dictionary.items(),
    'total_count':total_count, 'all_word_nspace':all_word_nspace, 'all_word':all_word,
    'max_count':max_count,'common_word':common_word,})