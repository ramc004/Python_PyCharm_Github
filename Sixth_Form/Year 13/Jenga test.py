import tkinter as tk
import random

import pygame


class JengaBlock:
    WIDTH = 60
    HEIGHT = 20

    def __init__(self, canvas, x, y, is_pulled=False):
        self.canvas = canvas
        self.is_pulled = is_pulled
        self.id = self.canvas.create_rectangle(x, y, x + self.WIDTH, y + self.HEIGHT, fill="saddle brown")

    def move(self, dx, dy):
        self.canvas.move(self.id, dx, dy)

    def is_pulled(self):
        return self.is_pulled

    def pull(self):
        self.is_pulled = True
        self.canvas.itemconfig(self.id, fill="black")


class JengaTower:
    def __init__(self, canvas, x, y, num_blocks):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.num_blocks = num_blocks
        self.blocks = []
        for i in range(num_blocks):
            block = JengaBlock(canvas, x, y + i * JengaBlock.HEIGHT)
            self.blocks.append(block)

    def get_top_block(self):
        for block in reversed(self.blocks):
            if not block.is_pulled:
                return block
        return None

    def pull_top_block(self):
        top_block = self.get_top_block()
        if top_block:
            top_block.pull()
            return top_block
        return None

    def move_top_block(self, dx, dy):
        top_block = self.get_top_block()
        if top_block:
            top_block.move(dx, dy)


class JengaGame:
    WIDTH = 400
    HEIGHT = 400

    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()

        self.tower = JengaTower(self.canvas, 50, 50, 18)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.dragging_block = None

    def on_click(self, event):
        block = self.tower.get_top_block()
        if block:
            x, y = event.x, event.y
            if x >= block.canvas.coords(block.id)[0] and x <= block.canvas.coords(block.id)[2] and \
                    y >= block.canvas.coords(block.id)[1] and y <= block.canvas.coords(block.id)[3]:
                self.dragging_block = block

    def on_drag(self, event):
        if self.dragging_block:
            dx, dy = event.x - self.last_x, event.y - self.last_y
            self.tower.move_top_block(dx, dy)
            self.last_x, self.last_y = event.x, event.y

    def on_release(self, event):
        if self.dragging_block:
            top_block = self.tower.get_top_block()
            if top_block and top_block != self.dragging_block:
                if abs(self.dragging_block.canvas.coords(self.dragging_block.id)[0] -
                       top_block.canvas.coords(top_block.id)[0]) < JengaBlock.WIDTH / 2:
                    self.dragging_block.move(0, JengaBlock.HEIGHT)
                    self.tower.pull_top_block()
                else:
                    self.dragging_block.move(0, -JengaBlock.HEIGHT)
            elif self.dragging_block:\
                self.dragging_block.move(0, pygame.mouse.get_pos()[1] - self.dragging_offset)
            self.dragging_block.draw(self.screen)