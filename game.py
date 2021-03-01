""" Módulo principal """

import pygame as pg
from engine import Engine, InputManager


def main():
    """ Função principal para a instância """
    resolution = (640, 480)

    engine = Engine(resolution)
    input_manager = InputManager(
        {
            pg.K_UP: "up",
            pg.K_DOWN: "down",
            pg.K_LEFT: "left",
            pg.K_RIGHT: "right",
            pg.K_SPACE: "select",
            1: "left_click",
            3: "right_click",
        }
    )

    surface = pg.Surface(resolution)

    while True:
        engine.tick()
        input_manager.update()
        engine.draw(surface)


if __name__ == "__main__":
    main()
