from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'wordcount/index.html')

def word_count(request):
    return render(request, 'wordcount/word_count.html')

def hello(request):
    entered_name = request.GET['name'] # 운영진님 피드백 : 변수명 name 수정
    return render(request, 'wordcount/hello.html', {'entered_name': entered_name})

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    word_list_count = len(word_list)

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    word_max_value = max(word_dictionary.values())
    
    word_max_key =[]
    for key, value in word_dictionary.items():
        if value == word_max_value:
            word_max_key.append(key)

    all_word_count = len(entered_text)
    space_count = entered_text.count(' ')
    nospace_word_count = all_word_count - space_count

    return render(request, 'wordcount/result.html', {'alltext' : entered_text, 'word_list_count' : word_list_count, 'word_max_key': word_max_key, 'word_max_value': word_max_value, 'all_word_count': all_word_count, 'nospace_word_count': nospace_word_count, 'dictionary' : word_dictionary.items()})


