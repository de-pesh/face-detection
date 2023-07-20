import pygame
from pygame.locals import *
from colors import *
from fonts import *
from security import *
        
def get_info():
    pygame.init()

    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Text Input Example')


    # Set up the textbox rectangle
    textbox_rect = pygame.Rect(50, 50, 300, 50)

    # Set up the OK button rectangle
    button_rect = pygame.Rect(150, 150, 100, 50)
    button_rect_shadow = pygame.Rect(147, 147, 106, 56)

    # Set up the initial text
    text = ''
    saved_text = None
    flag = False
    warn_text = ''
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    # Remove the last character from the text
                    text = text[:-1]
                else:
                    # Add the pressed character to the text
                    text += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # Save the text to a variable when the button is clicked
                    if text == '':
                        warn_text = 'warning:name can\'t be empty'
                        continue
                    elif check_name(text):
                        warn_text = 'warning: Invalid characters'
                        continue
                    saved_text = text
                    print("Saved Text:", saved_text)
                    flag = True
        if flag:
            break

        screen.fill(bg_color)

        # Draw the textbox rectangle
        eyn = font.render('Enter your name: ', True, text_color)
        screen.blit(eyn, (textbox_rect.x + 20  , textbox_rect.y - 40))
        
        pygame.draw.rect(screen, pygame.Color('lightgray'), textbox_rect,4,10)
        # Render the text
        text_surface = font.render(text, True, text_color)

        # Draw the text
        screen.blit(text_surface, (textbox_rect.x + 20, textbox_rect.y + 6))

        # Draw the OK button
        pygame.draw.rect(screen, pygame.Color('lightgrey'), button_rect_shadow,0,23)
        pygame.draw.rect(screen, pygame.Color('green'), button_rect,0,20)
        
        #warning text
        warn = w_font.render(warn_text, True, red)
        screen.blit(warn, (button_rect.x - 80, button_rect.y-40))

        
        button_text = font.render("OK", True, text_color)
        
        screen.blit(button_text, (button_rect.x + 25, button_rect.y + 6))

        pygame.display.flip()

    pygame.quit()
    return saved_text