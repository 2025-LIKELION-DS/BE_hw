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

    max_frequency = max(word_dictionary.values())
    most_frequent_words = [word for word, count in word_dictionary.items() if count == max_frequency]


    return render(request, 'result.html', {
        'most_frequent_word_count': max_frequency,
        'most_frequent_words': most_frequent_words,  # 리스트 형태로 전달
        'char_count_without_spaces': char_count_without_spaces,
        'word_count': word_count,
        'char_count': char_count,
        'alltext': entered_text,
        'dictionary': word_dictionary.items()
    })

def hello(request):
    name = request.GET.get('user_name')
    return render(request, 'hello.html', {'user_name': name})  