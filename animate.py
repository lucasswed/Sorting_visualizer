import pygame as pg
import random
from bogo import bogo_sort
from brick import brick_sort
from bubble import bubble_sort
from cocktail import cocktail_sort
from comb import comb_sort
from exchange import exchange_sort
from gnome import gnome_sort

COLORS = {
    "background": (35, 35, 40),
    "regular": (255, 248, 240),
    "highlight1": (239, 71, 111),
    "highlight2": (255, 209, 102),
    "highlight3": (17, 138, 178),
    "sorted": (6, 214, 160),
}

ALGORITHMS = {
    "Bogo Sort": bogo_sort,
    "Brick Sort": brick_sort,
    "Bubble Sort": bubble_sort,
    "Cocktail Sort": cocktail_sort,
    "Comb Sort": comb_sort,
    "Exchange Sort": exchange_sort,
    "Gnome Sort": gnome_sort
}


# Function to draw a single bar
def draw_bar(array, i, screen, color):
    n = len(array)
    (
        w,
        h,
    ) = screen.get_size()
    bar_width = w // n
    bar_height = h // n * array[i]
    x = bar_width * i
    y = h - bar_height
    bar = pg.Rect(x, y, bar_width, bar_height)
    pg.draw.rect(screen, color, bar)


# function to visualize an entire array using a bar chart
def draw_bars(array, screen, highlight1=[], highlight2=[], highlight3=[], sorted=False):
    screen.fill(COLORS["background"])
    n = len(array)
    if sorted:
        for i in range(n):
            draw_bar(array, i, screen, COLORS["sorted"])
    else:
        for i in range(n):
            draw_bar(array, i, screen, COLORS["regular"])
        for i in highlight1:
            draw_bar(array, i, screen, COLORS["highlight1"])
        for i in highlight2:
            draw_bar(array, i, screen, COLORS["highlight2"])
        for i in highlight3:
            draw_bar(array, i, screen, COLORS["highlight3"])
            
            
def animate(name, n = 50, speed = 10, width = 1500, height = 500, **kwargs):
    # Get algorithm from ditionary
    algorithm = ALGORITHMS[name]
    # Create array
    array = random.sample(range(1, n + 1), n)
    process = algorithm(array, **kwargs)

    pg.init()
    screen = pg.display.set_mode((width, height))
    
    pg.display.set_caption('Sorting algorithm visualization')
    
    font = pg.font.Font("freesansbold.ttf", 32)
    text = font.render(name, True, COLORS["regular"], COLORS["background"])
    text_box = text.get_rect(topleft=(10, 10))

    animation = True
    pausing = False
    while animation:

        if not pausing:
        
            # next_step in the sorting process
            array, highlight1, highlight2, highlight3 = next(process, (None, None, None, None))

            # Visualize the array using bar chart
            if array is not None:
                draw_bars(array, screen, highlight1, highlight2, highlight3)
            else:
                array = list(range(1, n + 1))
                draw_bars(array, screen, sorted=True)

            screen.blit(text, text_box)
            # update screen
            pg.display.flip()

            # pause
            pg.time.wait(1000 // speed)

        # track user interaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                animation = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    speed = max(1, speed - 1)

                if event.key == pg.K_RIGHT:
                    speed = min(100, speed + 1)

                if event.key == pg.K_SPACE:
                    pausing = not pausing

                if event.key == pg.K_RETURN:
                    array = random.sample(range(1, n + 1), n)
                    process = algorithm(array, **kwargs)
                    pausing = False

                if event.key == pg.K_ESCAPE:
                    animation = False
