""" This file is called "__main__.py". This is because it is the default filename that python looks for if you run it from the command line
    if you run `python .` in your terminal, it will run this file.
    you can ignore the orange comments like this ones if you want to but they are still useful.
"""

# green comments are pretty important though, you should read these as they are pretty straight forward

# import pygame
import pygame
# initialise all of it's modules (optional)
pygame.init()

# ask pygame to create a display with 512px width and 512px height
screen = pygame.display.set_mode([512, 512])

# set a global variable that stores the state of the game, this variable can be changed to exit the loop safely.
running = True
while running:
    """
        THIS RUNS EVERY FRAME
    """

    """
        here, we ask pygame for every event that has ran for the current frame, this can include keypresses and clicks / mouse movement and window close / window move
        pygame.event.get() returns a list of events which we loop over here, so we can iterate over that.
    """
    for event in pygame.event.get():

        # here we run a comparison check to see if the user has pressed the exit button on the top right of their display window

        # https://www.pygame.org/docs/ref/event.html you can scroll down on this page a bit and see some of the events that you can handle here.
        # (the yellow background text)
        if event.type == pygame.QUIT:
            # we handle that and close the program when that event fires by doing the following:
            # we set the variable for the main screen earlier to false to make sure that this is the last loop that will occur.
            running = False
            # the loop will continue after this line, until the end of this iteration then exit.
    """
        here we fill all of the pixels of the screen to a rgb color of 18, 18, 18 which is a very dark gray.
        this is ran ever frame so we can clear our frame, as we don't start with a blank frame, so if we drew on the window last frame, this will overwrite the drawings
    """
    screen.fill((18, 18, 18))

    # we can draw circles and all other kinds of shapes / images like this, there's more on this in other files
    
    """
        This function takes four parameters, the first one is the display we asked pygame to create with us, which was 512x512 pixels. We have to give this so pygame-
        knows which display to draw to. This is useful if you have multiple displays

        second parameter is the color of the shape we are drawing (as a tuple).
        if you want to be more advanced, you can also have a fourth value in this tuple which is the alpha of the color.

        the next variables vary upon the shape, as this is the circle:
            the third and the fourth variables are the center point and the radius (these are measured in pixels from the top left corner)
            there are alot more parameters that we can use for this, but these are the minimum we need to make a circle appear on the circle.

        you guys can also check out (you can ctrl+click this link:) https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        there is also intellisense, which i personally use and it saves you from going to reasearch online on what the things actually mean
        [on the sidebar there is a picture called intellisense.png which demonstrates this, it's very handy once you learn to read it]
    """
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # refresh the screen

    """
        whatever we did earlier was stored in a buffer, this buffer is stored in memory until you call this function, which updates the window
        this is sending all the drawings onto the window.
        you can try commenting this out and then running the program to see what happens.
    """
    pygame.display.flip()

# once the loop exits, you can clean up pygame and exit cleanly.
pygame.quit()
