from utils import randbool
from utils import randcell
from utils import randcells

CELL_TYPES = "🟩🌲🌊🏥🏭🔥"
BONUS = 100
UPD_COST = 5000
LIFE_COST = 7500
 
class Map:
    def __init__(self, w, h):
        self.w = w 
        self.h = h
        self.cell = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(4, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_updshop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        else: return True

    def print_map(self, helico, clouds):
        print("⬛️" * (self.w + 2))
        for ri in range(self.h):
            print("⬛️", end="")
            for ci in range(self.w):
                cell = self.cell[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print("☁️ ", end="")
                elif (clouds.cells[ri][ci] == 2):
                    print("🌩 ", end="")
                elif (helico.x == ri and helico.y == ci):
                    print("🚁", end="") 
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛️")
        print("⬛️" * (self.w + 2))

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cell[rx][ry] = 2
        while l > 0:
            rc2 = randcells(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cell[rx2][ry2] = 2 
                rx, ry = rx2, ry2 
                l -= 1 

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cell[ri][ci] = 1

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cell[cx][cy] == 0):
            self.cell[cx][cy] = 1

    def generate_updshop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cell[cx][cy] = 4
    
    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cell[cx][cy] != 4:
            self.cell[cx][cy] = 3
        else:
            self.generate_hospital()
    
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cell[cx][cy] == 1:
            self.cell[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cell[ri][ci]
                if cell == 5:
                    self.cell[ri][ci] = 0
        for i in range(10):
            self.add_fire()

    
    def process_helic(self, helico, clouds):
        c = self.cell[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2): 
            helico.tank = helico.maxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += BONUS
            self.cell[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPD_COST):
            helico.maxtank += 1
            helico.score -= UPD_COST
        if (c == 3 and helico.score >= LIFE_COST):
            helico.lives += 10
            helico.score -= LIFE_COST
        if (d == 2):
            helico.lives -= 1
            if (helico.lives == 0):
                helico.game_over()

    def export_data(self):
        return {"cell":  self.cell}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
