import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token='')
session_api = session.get_api() 
longpoll = VkLongPoll(session)



hello_list = ('И тебе привет!',
              'Привет',
              'Приветули красотули')

film_list = ('Маяк',
             'Веном',
             'Области тьмы',
             'Джон вик',
             'Титаник',
             'Джон Картер',
             'Выживший',
             'Джанго освобожденный',
             '12 друзей Оушена',
             'Омерзительная восьмерка',
             'Криминальное чтиво',
             'Форсаж',
             'Такси',
             'Хенкок',
             'Халк',
             'Каратель',
             'Хеллбой',
             'Назад в будущее',
             'Человек паук',
             'Бойцовский клуб')

photo_list = ('https://sun7-9.userapi.com/impg/nyQDiXAD0JgF0dA4rscgPgVn1403ScFTDvn4sA/xHUCooovMLk.jpg?size=1600x1066&quality=96&sign=40ec52131fe99f04d3d85ee942492af4&type=album',
              'https://sun7-7.userapi.com/impg/8DqWth6kcjvaZI0AzT2Xos1jVOVuW5e8GKOZPw/mXlrYnVaun4.jpg?size=1600x1066&quality=96&sign=368665aaa0a9126d3473eb03603fba79&type=album',
              'https://sun7-6.userapi.com/impg/iOgyP-1zErY6dV_m86IX3Z_jb1ifOU_mPBwqrA/h3whCXu_rGY.jpg?size=1280x1024&quality=96&sign=348e1e0fc1b52a5aff6634f37f2bf404&type=album',
              'https://sun7-8.userapi.com/impg/3Xtb703_LpSBTQNP4w4NFQoziy_cpTRC_H9XGQ/pQKUsl-MVis.jpg?size=950x623&quality=96&sign=30366564807ae454f1f915af92f5f8d0&type=album',
              'https://sun7-6.userapi.com/impg/MQrx9p-cn83U12qPNg1kgkYcMsv0QhzD8Pfskw/-_ggAtZwSIo.jpg?size=2048x1365&quality=96&sign=3ddd90ea867b68dbda6b0522363b9342&type=album',
              'https://sun7-7.userapi.com/impg/Ar9fQpf0-U9FORwbN7TQXJNU9BAmEnInYrZ5eg/cs2vxs6aDYM.jpg?size=2560x1440&quality=96&sign=c09f676a681267f6ad8e378dad73b821&type=album',
              'https://sun7-9.userapi.com/impg/LkYEGKDkDqgWV6Eous5s0SRql2UMntljxeAI_w/YkmdX9I4vy8.jpg?size=900x600&quality=96&sign=08c86d757f8865555a20501134f08a24&type=album',
              'https://sun7-6.userapi.com/impg/YYS7QBimwRNetV23on6x9jtgYyLMFSgrg3aETg/q5g94gsrC-Q.jpg?size=604x401&quality=96&sign=0b8798b6bd87b9fe98137dc28f71b3c6&type=album',
              'https://sun7-7.userapi.com/impg/pbsMJWED2tnRdfdUYnTJ9Tv7tUmATNamuGNNIg/0T9G0SYZErU.jpg?size=1280x853&quality=96&sign=2cfe36f7fbd29fbd19792ff878639300&type=album',
              'https://sun7-7.userapi.com/impg/b0n_VaXFPey6nvBnLS2NMpZewzVE_VBdalhMkQ/F1RzKO5Re0A.jpg?size=1200x800&quality=96&sign=83241f7bfd521fd28766f464da6e3021&type=album',
              'https://sun7-7.userapi.com/impg/_WUJMvdRnTGXthd6pgrVHLXuZIrmUnmnxofodQ/Vm7vWm0Lq5E.jpg?size=1200x801&quality=96&sign=0d4a7533b2a4c68643eda7b8f26b6915&type=album',
              'https://sun7-7.userapi.com/impg/wq-OXC6SzXQCEioi7c54NXIvJ9lqLiJ96y82yw/7JS1QrNIgeY.jpg?size=1558x2080&quality=96&sign=795c7eeb296d60c2563a95afff9d1aca&type=album',
              'https://sun7-7.userapi.com/impg/tnuN4-5iBfJEtuhwDMoyPUuPWEswQuz2X3fFxw/ilWQ-NsiPTo.jpg?size=1600x1066&quality=96&sign=3e1a1d5cc913ad05047fce23f84cd350&type=album',
              'https://sun7-9.userapi.com/impg/g4DTXva67nXvSS5QMlBUyxcTvo0oXyrnCXB4vQ/j0o083c0pfA.jpg?size=1066x1600&quality=96&sign=9ead71b23b559963faf65d577b1d8eb8&type=album',
              'https://sun7-7.userapi.com/impg/qDKyK0kJ1vp4DTj9seY75WyZ7mP4QHcMnQMQaA/tm1vfKucID8.jpg?size=1067x1600&quality=96&sign=d0185eeed092b08166196e8d15d6ec5b&type=album',
              'https://sun7-9.userapi.com/impg/8rWMVJg1CG1vWJXq6B-C0p6CLHxb0CS1hfkMyw/f1ZVCsjpzLA.jpg?size=1300x1203&quality=96&sign=28cdf55975b6264ee6de322db17a4dfb&type=album',
              'https://sun7-6.userapi.com/impg/_Hx_x_n2qYYNDUO7pGwLZbutJQv-SSN3b__eTA/w8A96H8Tlos.jpg?size=1200x800&quality=96&sign=e1ee2537563f3e0cf78cf4a4bd3e9938&type=album',
              'https://sun7-9.userapi.com/impg/_MCr51pESDgar7m0bcxAsJmNM7TUbwSPf6W3PQ/c8cJmziQmDc.jpg?size=1280x853&quality=96&sign=f8d8ce9068f38c7270b28f19c29cb521&type=album',
              'https://sun7-7.userapi.com/impg/ci5UymOAvtpaCRhWXMofa4SrM9OQIArjbVZ89Q/MHpw-IX27P4.jpg?size=1600x1055&quality=96&sign=bda0e7c8e9b132c8a175a319d372f2c9&type=album',
              'https://sun7-8.userapi.com/impg/p-KVFw1FlPUC9nXW2DH-yRA0Fpj0iU-XX7M-sg/jV_WeXIWp6E.jpg?size=1280x950&quality=96&sign=94a4f0054ddb443bf97791bb95e7da05&type=album',)



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
           print('Сообщение пришло в: ', event.datetime) 
           print('Текст сообщения: ', event.text)
           response = event.text.lower()
           if event.from_user and not event.from_me:
                if response.find('привет') >=0 or response.find('здравствуй') >=0 or response.find('хелоу') >=0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message': random.choice(hello_list),
                                    'random_id':'0'})
                elif response.find('как дела') >= 0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message': '',
                                    'random_id':'0',
                                    'sticker_id':'9045'})
                elif response.find('фото') >= 0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                    {'user_id':event.user_id,
                                    'message': random.choice(photo_list),
                                    'random_id':'0'})
                elif response.find('музыка') >= 0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message': '',
                                    'random_id':'0',
                                    'attachment':'audio347898216_456239040'})
                elif response.find('фильм') >= 0:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message': random.choice(film_list),
                                    'random_id':'0'})
                else:
                    time.sleep(random.uniform(0.5,3.0))
                    session.method('messages.send',
                                   {'user_id':event.user_id,
                                    'message': 'бубубу, я тебя не понял',
                                    'random_id':'0'})  
               
