def hello_who(name):
    return f'Hello, {name}'

def salary(hour,salary_by_hour):
        '''
        Рассчет зп сотрудника
        :param hours: количество часов
        :param by_hour: зарплата в час
        :return: итоговая сумма
        '''
        k = 2
        return hour * salary_by_hour * k
