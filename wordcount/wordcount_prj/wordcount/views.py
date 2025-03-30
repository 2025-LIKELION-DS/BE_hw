from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    result = sum(word_dictionary.values())

    except_text = entered_text.replace(" ", "")

    max_value = max(word_dictionary.values())

    return render(request, 'result.html', {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'word_sum': result, 'except_word': except_text, 'max_value': max_value})

def hello(request):
    user_name = request.GET['name']
    return render(request, 'hello.html', {'name': user_name})