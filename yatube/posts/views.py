from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts_list(request):
    return HttpResponse('Список блогеров')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, pk):
    return HttpResponse(f'Блогер под номером {pk}')
