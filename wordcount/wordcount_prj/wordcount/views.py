from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    return render(request, 'result.html')

def hello(request):
    entered_text = request.GET['fulltext']
    return render(request, 'hello.html', {'alltext': entered_text})


def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split() #입력받은 entered_text를 공백 기준으로 나누어서 단어 리스트 생성 

    word_count = len(word_list)

    text_without_spaces = entered_text.replace(" ", "")  # 공백을 제거
    char_count = len(text_without_spaces) #공백 제외 글자 수

    total_char_count = len(entered_text) #총 글자수수


    word_dictionary ={}
    for word in word_list: #단어 개수 세기
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
            word_dictionary[word] =1
    
    max_count = max(word_dictionary.values())  # 최대 빈도 값
    most_common_words = []

    for word, count in word_dictionary.items():
        if count == max_count:  # 최대 빈도와 동일한 단어를 추가
            most_common_words.append(word)



    return render(request, 'result.html', {'alltext': entered_text, 'dictionary':word_dictionary.items(), 
                                        'word_count': word_count, 'char_count':char_count, 
                                        'total_char_count': total_char_count,
                                        'most_common_words': most_common_words,
                                          'max_count': max_count,})
