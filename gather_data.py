# import cv2
# import pygame

# # Initialize Pygame
# pygame.init()

# # Set up the Pygame window
# window_size = (1280,720)
# window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Face Annotation")

# # Initialize the webcam
# capture = cv2.VideoCapture(0)

# # Variables for annotation
# start_point = None
# end_point = None
# annotate = False

# # Main program loop
# while True:
#     # Capture frame from the webcam
#     ret, frame = capture.read()

#     # Display the frame in the Pygame window
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     frame = cv2.flip(frame, 1)
#     frame = pygame.surfarray.make_surface(frame)
    
    
#     rotated_image = pygame.transform.rotate(frame, 270)
#     #new_rect = rotated_image.get_rect(center = frame.get_rect(topleft = 0).center)
#     screenUpdate = pygame.transform.scale(rotated_image, window_size)
    
#     window.blit(screenUpdate, (0,0))
#     pygame.draw.circle(window, (0,0,0), [640, 650], 30)
#     pygame.draw.circle(window, (255,255,255), [640, 650], 25)
#     pygame.draw.circle(window, (0,0,0), [640, 650], 23)
    
#     #window.blit(frame, (0, 0))
#     pygame.display.update()

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             capture.release()
#             cv2.destroyAllWindows()
#             exit()

#         # Start annotation when the left mouse button is pressed
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             start_point = event.pos
#             annotate = True

#         # End annotation and save the annotated image when the left mouse button is released
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             end_point = event.pos
#             annotate = False

#             # Save the annotated image
#             face_img = frame.copy()
#             face_img = pygame.surfarray.array3d(face_img)
#             face_img = cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR)
#             cv2.rectangle(face_img, start_point, end_point, (0, 255, 0), 2)
#             cv2.imwrite("annotated_face.jpg", face_img)


#     if annotate:
#         end_point = pygame.mouse.get_pos()
#         pygame.draw.rect(window, (0, 255, 0), (start_point, (end_point[0] - start_point[0], end_point[1] - start_point[1])), 2)
#         pygame.display.update()



import cv2
import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_size = (1280,720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Face Annotation")

# Initialize the webcam
capture = cv2.VideoCapture(0)

# Variables for annotation
start_point = None
end_point = None
annotate = False

# Variables for photo capturing
capture_counter = 0
photo_folder = "photos"  # Custom folder name

# Create the folder if it doesn't exist
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Main program loop
while True:
    # Capture frame from the webcam
    ret, frame = capture.read()

    # Display the frame in the Pygame window
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    frame = pygame.surfarray.make_surface(frame)
    
    
    rotated_image = pygame.transform.rotate(frame, 270)
    # new_rect = rotated_image.get_rect(center = frame.get_rect(topleft = 0).center)
    screenUpdate = pygame.transform.scale(rotated_image, window_size)

    window.blit(screenUpdate, (0, 0))
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            capture.release()
            cv2.destroyAllWindows()
            exit()

        # Start annotation when the left mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_point = event.pos
            annotate = True

        # End annotation and save the annotated image when the left mouse button is released
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            end_point = event.pos
            annotate = False

            # Save the annotated image
            face_img = frame.copy()
            face_img = pygame.surfarray.array3d(face_img)
            face_img = cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR)
            cv2.rectangle(face_img, start_point, end_point, (0, 255, 0), 2)

            # Save the annotated image in the photos folder
            photo_name = f"{photo_folder}/annotated_face_{capture_counter}.jpg"
            cv2.imwrite(photo_name, face_img)
            print(f"Saved photo: {photo_name}")

            # Increase the capture counter
            capture_counter += 1

            # If 5 photos have been captured, exit the program
            if capture_counter == 5:
                pygame.quit()
                capture.release()
                cv2.destroyAllWindows()
                exit()

    # Annotate the face in real-time
    if annotate:
        end_point = pygame.mouse.get_pos()
        pygame.draw.rect(window, (0, 255, 0), (start_point, (end_point[0] - start_point[0], end_point[1] - start_point[1])), 2)
        pygame.display.update()
