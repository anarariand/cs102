import pathlib
import random
import copy
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, size: Tuple[int, int], randomize: bool=True, max_generations: Optional[int]=None) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.n_generation = 1

    def create_grid(self, randomize: bool=False) -> Grid:
        grid = []
        for i in range(self.rows):
            sub_array = []
            for j in range(self.cols):
                sub_array.append(randomize * random.randint(0, 1))
            grid.append(sub_array)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.
        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.
        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.
        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        x, y = cell
        cells = []
        if x - 1 >= 0 and y - 1 >= 0:
            cells.append(self.curr_generation[x - 1][y - 1])
        if x - 1 >= 0:
            cells.append(self.curr_generation[x - 1][y])
        if x - 1 >= 0 and y + 1 < self.cols:
            cells.append(self.curr_generation[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.curr_generation[x][y - 1])
        if y + 1 < self.cols:
            cells.append(self.curr_generation[x][y + 1])
        if x + 1 < self.rows and y + 1 < self.cols:
            cells.append(self.curr_generation[x + 1][y + 1])
        if x + 1 < self.rows and y - 1 >= 0:
            cells.append(self.curr_generation[x + 1][y - 1])
        if x + 1 < self.rows:
            cells.append(self.curr_generation[x + 1][y])
        return cells     

    def get_next_generation(self) -> Grid:
        new_grid = copy.deepcopy(self.curr_generation)
        for i in range(len(self.curr_generation)):
            for j in range(len(self.curr_generation[i])):
                neighbours = self.get_neighbours((i, j)).count(1)
                if neighbours == 3:
                    new_grid[i][j] = 1
                elif neighbours == 2 and self.curr_generation[i][j] == 1:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
        self.n_generation += 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()

    @property
    def is_max_generations_exceed(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.n_generation >= self.max_generations     #type:ignore

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(filename, 'r')
        grid = []
        strings = f.read().split('\n')
        rows = len(strings)
        cols = len(strings[0])
        strings = strings[:-1]
        for s in strings:
            sub_array = []
            for char in s:
                sub_array.append(int(char))
            grid.append(sub_array)
        game = GameOfLife((rows, cols), False)
        game.curr_generation = copy.deepcopy(grid)
        f.close()
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        f = open(filename, 'w')
        for s in self.curr_generation:
            for item in s:
                f.write(str(item).replace("'", ''))
            f.write('\n')