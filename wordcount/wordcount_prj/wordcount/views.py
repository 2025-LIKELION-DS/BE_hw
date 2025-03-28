from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcount/index.html')

def word_count(request):
    return render(request, 'wordcount/word_count.html')

def result(request):
    entered_text = request.GET["fulltext"]  # 입력된 전체 텍스트
    word_list = entered_text.split()  # 단어 단위로 분할

    word_dictionary = {}  # 단어 빈도를 저장할 딕셔너리
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    # 공백 포함 글자 수
    char_count_with_spaces = len(entered_text)

    # 공백 제외 글자 수
    char_count_without_spaces = len(entered_text.replace(" ", ""))

    # 가장 많이 입력된 단어 찾기
    if word_dictionary:
        max_word_count = max(word_dictionary.values())  # 가장 큰 빈도수 찾기
        max_words = [word for word, count in word_dictionary.items() if count == max_word_count]  # 최빈 단어 리스트
    else:
        max_words = []
        max_word_count = 0

    return render(
        request,
        "wordcount/result.html",
        {
            'alltext': entered_text,
            'dictionary': word_dictionary.items(),
            'word_count': len(word_list),
            'char_count_with_spaces': char_count_with_spaces,
            'char_count_without_spaces': char_count_without_spaces,
            'max_words': max_words,
            'max_word_count': max_word_count,
        }
    )


def hello(request):
    name_text = request.GET["nametext"]
    return render(request,"wordcount/hello.html",{'yourname':name_text})
