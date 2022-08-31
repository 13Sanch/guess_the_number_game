import numpy as np # Импортируем библиотеку в переменную 

"""Игра угадай число, компьютер сам загадывает, сам угадывает меньше или за 20 попыток"""

def random_predict(number:int=1) -> int: # Фунция должна получать число 
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное компьютером число. Defaults to 1.

    Returns:
        int: Количество попыток 
    """
    
    count_attempts = 0 # Количество попыток 
    number = 1 # Начальное число 
    predict_number = np.random.randint(1, 101) # Присваиваем переменной загаданное число
    while number != predict_number: # Цикл будет выполняться пока условие неравенства истино 
        if number < predict_number:
            number += 10 # Если число меньше загаданного, увеличиваем начальное число 
            count_attempts += 1 # Увеличиваем количество попыток 
        
        elif number > predict_number:
            number -= 1 # Если число стало больше искомого 
            count_attempts += 1 # Увеличиваем количество попыток 
        
        else:
            break # Если число и искомое число совпадают, прерываем цикл
    return count_attempts

def score_game(random_predict) -> int: # Функция повторяет и записывает результат за 1000 повторений 
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм загаданное число

    Args:
        random_predict (_type_): Функция угадывания 

    Returns:
        int: Среднее количество попыток
    """
    
    count_list = [] # Список для хранения количества попыток 
    np.random.seed(1) # Фиксируем сид для воспроизведения 
    random_array = np.random.randint(1, 101, size=(1000)) # Присваиваем переменной список загаданных чисел 
    
    
    for number in random_array: 
        count_list.append(random_predict(number)) # Добавляем в список количество попыток на угадывание числа 
    
    score = int(np.mean(count_list)) # Находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток') # Выводим информацию о среднем количестве попыток 
    return score # Возвращаем результат среднего количества попыток 

print(score_game(random_predict)) # Выводим на экран функцию 