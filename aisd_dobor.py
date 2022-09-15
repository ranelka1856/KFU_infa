# наш лабиринт в виде двумерного массива,
# где 0 означает проход, а -1 - стену,
# передвигаться по диагонали нельзя
maze = [
    [0, -1,  0,  0],
    [0, -1, -1, -1],
    [0,  0,  0, -1],
    [0, -1,  0,  0],
]

# обозначаем начало и конец
start_point = (0, 0)
end_point = (3, 3)


# получаем размеры лабиринта
n = len(maze)
m = len(maze[0])


def pretty_view():
    """ Вывести лабиринт в консоль """
    for line in maze:
        for n in line:
            print(n, end='\t')
        print()


def get_point(p):
    """ Функция для получения значения клетки"""
    if p[0] not in range(n) or p[1] not in range(m):
        return None
    return maze[p[0]][p[1]]


def get_beside(x, y):
    """ Возвращает координаты потенциальных соседей """

    # если нельзя двигаться по диагонали
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    # если можно двигаться по диагонали
    # result = []
    # for i in range(x-1, x+2):
    #     for j in range(y-1, y+2):
    #         result.append((i, j))
    # return result


def wave_alg():
    """ Волновой алгоритм """

    # Часть первая: покраска лабиринта

    # здесь хранится очередь на обработку
    queue = [(start_point, 1)]
    while len(queue) != 0:
        data = queue.pop(0)
        # на каждой итерации мы помечаем нашу клетку
        # и добавляем в очередь все соседние
        result = wave_alg_(data[0], data[1])
        # но уже с меткой на единицу больше
        for r in result:
            queue.append((r, data[1]+1))

    # Часть вторая: восстанавливаем путь с конца

    if get_point(end_point) == 0:
        # если конец лабиринта не был отмечен,
        # значит до него нельзя добраться
        # возвращаем None
        return None

    # идем с конца: добавляем в наш путь конечную точку
    path = [end_point]

    # цикл работает пока мы не дойдем то старта
    while path[-1] != start_point:
        # берем последнюю точку
        p = path[-1]
        # и ищем среди её соседей тех, у которых
        # значение на единицу меньше;
        # то есть соседей, с которых мы можем добраться
        # до этой точки
        for point in get_beside(p[0], p[1]):
            v = get_point(point)
            if v and v == get_point(p) - 1:
                path.append(point)
                break

    # в итоге мы определили путь от конца до начала,
    # возвращаем обратный путь (от начала до конца)
    return path[::-1]


def wave_alg_(point, cur_gen):
    """ Функция для покраски клетки """

    # отмечаем нашу клетку
    maze[point[0]][point[1]] = cur_gen

    # и возвращаем все соседние (но еще не отмеченные)
    result = []
    for point in get_beside(point[0], point[1]):
        v = get_point(point)
        if v == 0:
            result.append(point)
    return result


print('лабиринт до покраски:')
pretty_view()
path = wave_alg()
print('лабиринт после покраски, теперь можно отследить путь от начала до конца:')
pretty_view()
print('путь:', path)
