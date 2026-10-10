import math
from array import array

import pygame
from .round import Round

# Game Engine

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (90, 90, 90)
GREEN = (40, 180, 90)
BLUE = (50, 90, 170)


def _make_tone(frequency, duration_ms):
    """Create a short sine-wave sound using the active mixer format."""
    mixer_settings = pygame.mixer.get_init()
    if mixer_settings is None:
        raise pygame.error("The audio mixer is unavailable")

    sample_rate, sample_format, channels = mixer_settings
    if sample_format != -16:
        raise ValueError("Only signed 16-bit mixer audio is supported")

    frame_count = int(sample_rate * duration_ms / 1000)
    fade_frames = max(1, int(sample_rate * 0.01))
    samples = array("h")

    for frame in range(frame_count):
        fade = min(
            1,
            frame / fade_frames,
            (frame_count - frame - 1) / fade_frames,
        )
        wave = math.sin(2 * math.pi * frequency * frame / sample_rate)
        sample = int(32767 * 0.25 * fade * wave)
        for _ in range(channels):
            samples.append(sample)

    return pygame.mixer.Sound(buffer=samples.tobytes())


class GameEngine:
    def __init__(
        self,
        width,
        height,
        rounds_total=5,
        min_wait_ms=1000,
        max_wait_ms=3000
    ):
        self.width = width
        self.height = height

        self.rounds_total = rounds_total
        self.min_wait_ms = min_wait_ms
        self.max_wait_ms = max_wait_ms
        self.difficulty = "Medium"

        self.round = Round(self.min_wait_ms, self.max_wait_ms)
        self.reaction_times = []

        self.result_shown_at = None
        self.result_pause_ms = 800

        self.font = pygame.font.SysFont("Arial", 24)
        self.big_font = pygame.font.SysFont("Arial", 42)

        self.game_over = False
        self.sounds = {}
        self._initialize_sounds()

        button_y = self.height - 85
        self.easy_button = pygame.Rect(20, button_y, 150, 42)
        self.medium_button = pygame.Rect(
            self.width // 2 - 75, button_y, 150, 42
        )
        self.hard_button = pygame.Rect(
            self.width - 170, button_y, 150, 42
        )
        self.exit_button = pygame.Rect(
            self.width // 2 - 75, self.height - 38, 150, 30
        )

    def _initialize_sounds(self):
        try:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init(frequency=22050, size=-16, channels=1)

            self.sounds = {
                "go": _make_tone(880, 140),
                "false_start": _make_tone(220, 260),
                "session_end": _make_tone(660, 360),
            }
        except (pygame.error, ValueError):
            # Sound is optional; keep the game playable without an audio device.
            self.sounds = {}

    def _play_sound(self, name):
        sound = self.sounds.get(name)
        if sound is not None:
            try:
                sound.play()
            except pygame.error:
                # An audio device can become unavailable while the game runs.
                pass

    def handle_event(self, event):
        if self.game_over:
            self.handle_menu_click(event)
            return

        is_click = event.type == pygame.MOUSEBUTTONDOWN
        is_space = (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
        )

        if not (is_click or is_space):
            return

        if self.round.state in ("result", "false_start"):
            return

        reaction_ms = self.round.register_input()

        if self.round.state == "false_start":
            self._play_sound("false_start")

        # Store valid reaction times only.
        if reaction_ms is not None:
            self.reaction_times.append(reaction_ms)

        self.result_shown_at = pygame.time.get_ticks()

    def handle_input(self):
        pass

    def update(self):
        if self.game_over:
            return

        was_waiting = self.round.state == "waiting"
        self.round.update()
        if was_waiting and self.round.state == "go":
            self._play_sound("go")

        if self.round.state in ("result", "false_start"):
            now = pygame.time.get_ticks()

            if (
                self.result_shown_at is not None
                and now - self.result_shown_at >= self.result_pause_ms
            ):
                self._start_next_round()

    def _start_next_round(self):
        if len(self.reaction_times) >= self.rounds_total:
            self.game_over = True
            self._play_sound("session_end")
            return

        self.round = Round(self.min_wait_ms, self.max_wait_ms)
        self.result_shown_at = None

    def average_reaction_ms(self):
        if not self.reaction_times:
            return 0

        return round(
            sum(self.reaction_times) / len(self.reaction_times)
        )

    def set_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.min_wait_ms = 1500
            self.max_wait_ms = 3000
            self.rounds_total = 5

        elif difficulty == "Medium":
            self.min_wait_ms = 1000
            self.max_wait_ms = 2500
            self.rounds_total = 5

        elif difficulty == "Hard":
            self.min_wait_ms = 500
            self.max_wait_ms = 1500
            self.rounds_total = 5

        self.difficulty = difficulty

    def restart_game(self, difficulty):
        self.set_difficulty(difficulty)

        self.round = Round(self.min_wait_ms, self.max_wait_ms)
        self.reaction_times = []
        self.result_shown_at = None
        self.game_over = False

    def handle_menu_click(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        x, y = event.pos

        # Difficulty buttons.
        if self.easy_button.collidepoint(x, y):
            self.restart_game("Easy")

        elif self.medium_button.collidepoint(x, y):
            self.restart_game("Medium")

        elif self.hard_button.collidepoint(x, y):
            self.restart_game("Hard")

        elif self.exit_button.collidepoint(x, y):
            pygame.quit()
            raise SystemExit

    def render(self, screen):
        screen.fill(WHITE)

        if self.game_over:
            title = self.big_font.render("Game Over!", True, BLACK)
            screen.blit(
                title,
                title.get_rect(center=(self.width // 2, 35))
            )

            # Show reaction times.
            y = 75
            for index, reaction_ms in enumerate(self.reaction_times, start=1):
                result_text = self.font.render(
                    f"Round {index}: {reaction_ms} ms",
                    True,
                    BLACK
                )
                screen.blit(
                    result_text,
                    result_text.get_rect(center=(self.width // 2, y))
                )
                y += 27

            # Show average.
            average_text = self.font.render(
                f"Average: {self.average_reaction_ms()} ms",
                True,
                BLACK
            )
            screen.blit(
                average_text,
                average_text.get_rect(center=(self.width // 2, y + 3))
            )

            for button, label in [
                (self.easy_button, "Easy"),
                (self.medium_button, "Medium"),
                (self.hard_button, "Hard")
            ]:
                pygame.draw.rect(screen, GREEN, button, border_radius=8)
                text = self.font.render(label, True, WHITE)
                screen.blit(text, text.get_rect(center=button.center))

            pygame.draw.rect(screen, BLUE, self.exit_button, border_radius=6)

            exit_text = self.font.render("Exit", True, WHITE)
            screen.blit(exit_text, exit_text.get_rect(center=self.exit_button.center))
            return

        # Normal gameplay screen.
        if self.round.state == "waiting":
            bg = GRAY
            message = "Wait for green..."

        elif self.round.state == "go":
            bg = GREEN
            message = "Click now!"

        elif self.round.state == "false_start":
            bg = BLUE
            message = "False start! Wait for green."

        else:
            bg = BLUE
            message = f"{self.round.reaction_ms} ms"

        screen.fill(bg)

        text_surf = self.big_font.render(message, True, WHITE)
        text_rect = text_surf.get_rect(
            center=(self.width // 2, self.height // 2)
        )
        screen.blit(text_surf, text_rect)

        round_num = min(len(self.reaction_times) + 1, self.rounds_total)
        round_text = self.font.render(
            f"Round {round_num}/{self.rounds_total}", True, WHITE
        )
        screen.blit(round_text, (10, 10))

        avg_text = self.font.render(
            f"Avg: {self.average_reaction_ms()} ms", True, WHITE
        )
        screen.blit(avg_text, (self.width - 190, 10))