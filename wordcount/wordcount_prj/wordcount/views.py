from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request,'word_count.html')

def result(request):

    entered_text=request.GET['fulltext']
    word_list=entered_text.split()

    word_count=len(word_list)
    char_count = len(entered_text)
    char_count_without_spaces = len(entered_text.replace(" ", ""))

    word_dictionary={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    most_frequent_word = max(word_dictionary, key=word_dictionary.get)
    most_frequent_word_count = word_dictionary[most_frequent_word]

    return render(request, 'result.html', {'most_frequent_word_count': most_frequent_word_count,'most_frequent_word': most_frequent_word,'char_count_without_spaces': char_count_without_spaces,'word_count':word_count,'char_count': char_count,'alltext':entered_text,'dictionary':word_dictionary.items()})

def hello(request):
    name = request.GET.get('user_name')
    return render(request, 'hello.html', {'user_name': name})  