import sys
def create_blank_map():
    mmap = [[set() for x in range (9)] for y in range (9)]
    return mmap

def check_hor(puzzle, i, values_left):
    for value in range (9):
        values_left.discard(puzzle[i][value])
    print ("scanned horizontally")

def check_vert(puzzle, j, values_left):
    for value in range (9):
        values_left.discard(puzzle[value][j])
    print ("scanned vertically")

def check_box(puzzle, i, j, values_left):
    i = int (i/3) * 3
    j = int (j/3) * 3
    smallbox = ReturnNextField(3, i, j)
    while True:
        try:
            values_left.discard(puzzle[i][j])
            i, j = smallbox.__next__()
        except StopIteration:
            print ("scanned box")
            break


class ReturnNextField:
    # new_iter = True
    # itercount = 1
    # puzzlecache = [[False for x in range(9)] for y in range(9)]
    def __init__(self, box, i, j, is_solved = True):
        self.box = box
        self.i = i
        self.j = j
        self.min_i = i
        self.min_j = j
        self.max_i = i + box - 1
        self.max_j = j + box - 1
        # self.is_solved = is_solved
    def __iter__(self):
        return self
    def prev(self):
        self.j += 1
        if self.j > self.max_j:
            self.i += 1
            self.j = self.min_j
            self.new_iter = False

            if self.i > self.max_i:
                # if self.is_solved:
                    raise StopIteration
                # else:
                #     self.is_solved = True
                #     self.new_iter = True
                #     self.itercount += 1
                #     self.i = 0
                #     self.j = 0
        return self.i, self.j
    def __next__(self):
        if self.i == self.min_i and self.j == self.min_j:
            return self.i, self.j

        self.j -=1
        if self.j < self.min_j:
            self.i -= 1
            self.j = self.max_j
        return self.i, self.j


def stepbystep(puzzle, i, j, bigbox, tried_values=[[set() for x in range(9)] for y in range(9)],
               back_flag=False):
    try:
        print("******")
        print("Currently at ", i, ",", j)


        # Skip this field if value is present at default
        if puzzle[i][j]:
            if puzzle[i][j] not in tried_values[i][j]:
                if back_flag:
                        i, j = bigbox.prev()
                        stepbystep(puzzle, i, j, bigbox, tried_values, back_flag=True)
                        return
                else:
                    i, j = next(bigbox)
                    stepbystep(puzzle, i, j, bigbox, tried_values)
                    return

        available_values = set(range(1,10))

        #Check possible values based on puzzle
        check_hor(puzzle, i, available_values)
        check_vert(puzzle, j, available_values)
        check_box(puzzle, i, j, available_values)

        #Check the values that have been tried before
        available_values.difference_update(tried_values[i][j])
        for tried in tried_values[i][j]:
            print ("I have tried: ",tried)
        print("I can try ", available_values)

        #backtrack if no possible input values
        if not available_values:
            print("backtracking..")
            puzzle[i][j] = 0
            tried_values[i][j] = set()
            i, j = bigbox.prev()
            stepbystep(puzzle, i, j, bigbox, tried_values, True)

        #skip if there are 3 possible options
        # elif len(available_values) > 2:
        #     print("skip this sh!t")
        #     bigbox.is_solved = False
        #     if back_flag:
        #         i, j = bigbox.prev()
        #         stepbystep(puzzle, i, j, bigbox, tried_values, back_flag= True)
        #     else:
        #         i, j = next(bigbox)
        #         stepbystep(puzzle, i, j, bigbox, tried_values)

        #place a value into the puzzle.
        else:
            value_to_try = available_values.pop()
            tried_values[i][j].add(value_to_try)
            puzzle[i][j] = value_to_try
            print ("Placing ", value_to_try, "at " , i, ",", j)
            print ("*****")
            i, j = next(bigbox)
            stepbystep(puzzle, i, j, bigbox, tried_values)
    except RecursionError:
        pass

def sudoku_solve_reverse(puzzle):
    sys.setrecursionlimit(3000)
    bigbox = ReturnNextField(9, 8, 8)
    try:
        stepbystep(puzzle, 8, 8, bigbox, )
    except StopIteration:
        for row in puzzle:
            print(row)
        return puzzle

if __name__ == '__main__':
    puzzle_unsolved = [
                       [3,0,9,0,0,5,0,0,8],
                       [0,0,0,8,7,0,2,0,3],
                       [0,0,0,0,0,0,5,0,0],
                       [0,6,1,0,0,9,0,0,0],
                       [0,0,0,7,6,0,0,0,0],
                       [8,0,2,0,0,0,0,5,0],
                       [2,0,0,3,0,0,0,0,0],
                       [0,7,0,0,0,0,0,0,0],
                       [0,5,0,0,9,0,6,3,0],
                       ]
    sudoku_solve(puzzle_unsolved)