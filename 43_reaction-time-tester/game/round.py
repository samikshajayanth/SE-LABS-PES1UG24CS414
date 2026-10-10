import random
import pygame


class Round:
    def __init__(self, min_wait_ms=1000, max_wait_ms=3000):
        self.wait_delay_ms = random.randint(min_wait_ms, max_wait_ms)
        self.state = "waiting"
        self.start_time = pygame.time.get_ticks()
        self.go_time = None
        self.reaction_ms = None

    def update(self):
        if self.state == "waiting":
            now = pygame.time.get_ticks()

            if now - self.start_time >= self.wait_delay_ms:
                self.state = "go"
                self.go_time = now

    def register_input(self):
        if self.state in ("result", "false_start"):
            return None

        if self.state == "waiting":
            self.reaction_ms = None
            self.state = "false_start"
            return None

        if self.state == "go":
            now = pygame.time.get_ticks()
            self.reaction_ms = now - self.go_time
            self.state = "result"
            return self.reaction_ms

        return None