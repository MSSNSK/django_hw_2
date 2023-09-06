from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page')
    return HttpResponse('<h1 style="text-align: center">Главная страница о моём первом Django сайте.</h1>'
                        '<p style="text-align: center">Многострочный текст с HTML вёрсткой и данными о моём первом '
                        'Django сайте...</p>')


def about(request):
    logger.info('About')
    return HttpResponse('<h1 style="text-align: center">Страница обо мне.</h1>'
                        '<p style="text-align: center">Многострочный текст с HTML вёрсткой и данными обо мне...</p>')
