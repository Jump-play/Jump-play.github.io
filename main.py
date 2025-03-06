import asyncio
import pygame
# Try to declare all your globals at once to facilitate compilation later.
COUNT_DOWN = 3

# Do init here
# Load any assets right now to avoid lag at runtimepygame.mixer.music.load('assets/assets_boss.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
jump_fx = pygame.mixer.Sound('assets/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/death.mp3')
death_fx.set_volume(0.5)or network errors.


async def main():
    global COUNT_DOWN

    # avoid this kind declaration, prefer the way above
    COUNT_DOWN = 3

    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices

        print(f"""

            Hello[{COUNT_DOWN}] from Python

""")
        # pygame.display.update() should go right next line

        await asyncio.sleep(0)  # Very important, and keep it 0

        if not COUNT_DOWN:
            return

        COUNT_DOWN = COUNT_DOWN - 1

# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()
