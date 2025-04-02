from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcount/index.html')

def word_count(request):
    return render(request, 'wordcount/word_count.html')

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    total_word_count = len(word_list)
    total_char_count = len(entered_text)
    char_no_space = len(entered_text.replace(" ",""))

    max_freq = max(word_dictionary.values())
    most_frequent_words = [word for word, freq in word_dictionary.items() if freq == max_freq]
    return render(request, 'wordcount/result.html', {'alltext':entered_text, 'dictionary':word_dictionary.items(), 'total' : total_word_count,
    'total_chars': total_char_count, 'no_space': char_no_space, 'most_words': most_frequent_words, 'max_freq': max_freq,})

def hello(request):
    name = request.GET.get('name')
    return render(request, 'wordcount/hello.html', {'username': name})