'''
Name: Rahul Iyer
Teacher: Mr.Ghorvei
Date: June 22nd, 2021
Assignment: Python Assignment 2
'''
#-------------------------------------------------------------------------------------------------------------------------------

# Function to center a position with given sizes
def center(pos, size1, size2):
    # Return centered position
    return (pos+size1/2) - (size2/2)
# imports the library, turns on and off the system in pygame
import sys
import pygame
from pygame import time
from pygame import mouse
import random
from pygame import display
from pygame.constants import MOUSEBUTTONDOWN

# begins running the initial variables within pygame
pygame.init()
pygame.font.init()
# determines the size of the page in pygame
size = width, height = 1280, 720
# sets the screen for the pygame
screen = pygame.display.set_mode(size)
# while statement for the whole website, when it is open it runs, if not open then pygame will not function

# Color variables for background
bkgClr = (53, 137, 161)
# Color variable for bar
barClr = (52, 152, 180)

# Set the display caption of the window
pygame.display.set_caption('Movie Ticket System')


# Load the image, scale the image
arrowImg = pygame.image.load("arrow.png")
arrowImg = pygame.transform.scale(arrowImg, (150, 140))
# Get the rectangle, and center image
arrowImgRect = arrowImg.get_rect()
arrowImgRect.x = width/2-(-330)
arrowImgRect.y +=160

# Godzilla vs Kong Poster
# Load the image, scale the image
godzillaImg = pygame.image.load("Godzilla vs Kong.jpg")
godzillaImg = pygame.transform.scale(godzillaImg, (230, 340))
# Get the rectangle, and center image
godzillaImgRect = godzillaImg.get_rect()
godzillaImgRect.x = width/2-620
godzillaImgRect.y += 325

# Spider-Man 3 Poster
# Load the image, scale the image
spidermanImg = pygame.image.load('spider-man 3.jpeg')
spidermanImg = pygame.transform.scale(spidermanImg, (230, 340))
# Get the rectangle, and center image
spidermanImgRect = spidermanImg.get_rect()
spidermanImgRect.x = width/2-370
spidermanImgRect.y += 325

# Avengers: Infinity War poster
# Load the image, scale the image
avengersImg = pygame.image.load('AvengersIW.jpg')
avengersImg = pygame.transform.scale(avengersImg, (230, 340))
# Get the rectangle, and center image
avengersImgRect = avengersImg.get_rect()
avengersImgRect.x = width/2-120
avengersImgRect.y += 325

# Interstellar Poster
# Load the image, scale the image
interstellarImg = pygame.image.load('interstellar.jpg')
interstellarImg = pygame.transform.scale(interstellarImg, (230, 340))
# Get the rectangle, and center image
interstellarImgRect = interstellarImg.get_rect()
interstellarImgRect.x = width/2-(-130)
interstellarImgRect.y += 325

# Inception Poster
# Load the image, scale the image
inceptionImg = pygame.image.load('inception.png')
inceptionImg = pygame.transform.scale(inceptionImg, (230, 340))
# Get the rectangle, and center image
inceptionImgRect = inceptionImg.get_rect()
inceptionImgRect.x = width/2-(-380)
inceptionImgRect.y += 325

# List containing all images in program
movieImg = [godzillaImg, spidermanImg, avengersImg, interstellarImg, inceptionImg]
# List contained all rectangles of images
movieRect = [godzillaImgRect, spidermanImgRect, avengersImgRect, interstellarImgRect, inceptionImgRect]
# List containing all movie names
movies = ["Godzilla vs. Kong", "Spiderman 3", "Avengers Infinity War", "Interstellar", "Inception"]

# User icon
# Load the image, scale the image
iconImg = pygame.image.load('user icon.png')
iconImg = pygame.transform.scale(iconImg, (30, 30))
# Get the rectangle, and center image
iconImgRect = iconImg.get_rect()
iconImgRect.x = width/2-(-605)
iconImgRect.y = center(0, 50, iconImgRect.height)

# Set the color of the logo
logoClr = (40, 255, 13)
# Get the font, and render the font with specified color
logoFont = pygame.font.Font("Horta demo.otf", 115)
logo = logoFont.render("MOVIEFLEX", True, logoClr)
# Get the rectangle, and center image
logoRect = logo.get_rect()
logoRect.x = (width/2)-logoRect.width/2
logoRect.y += 15

# Cinema Picture
# Load the image, scale the image
cinemaImg = pygame.image.load("cinema.png")
cinemaImg = pygame.transform.scale(cinemaImg, (190, 240))
# Get the rectangle, and center image
cinemaImgRect = cinemaImg.get_rect()
cinemaImgRect.x = width/2-(-150)
cinemaImgRect.y +=-50

# Color for account text
acctClr = (255, 213, 0)
# Get the font, and render the font with specified color
acctFont = pygame.font.Font("Horta demo.otf", 59)
acct = acctFont.render(
    "DO YOU HAVE A PRE-EXISTING ACCOUNT?", True, acctClr)
# Get the rectangle, and center image
acctRect = acct.get_rect()
acctRect.x = (width/2)-acctRect.width/2
acctRect.y += 350

# Variables to control when to show login and signup
showLogin = False
showSignin = False

# Variables for the buffers
mouseBuffer = True
inputBuffer = True
keyBuffer = True

# Variable containing the username and password
username = ''
password = ''

# Variable for controlling when to type on the username and password
typeUsername = False
typePassword = False

# List containing all usernames and passwords
usernames = []
passwords = []

# Opening the loginInfo text file
f = open("loginInfo.txt", "r")
# For loop for each line in the file
for line in f:
    # If the line starts with 'u', it is a username
    if line[0] == 'u':
        # Append username to username list
        usernames.append(line[2:].rstrip())
    
    # If the line starts with 'p', it is a password
    elif line[0] == 'p':
        # Append password to password list
        passwords.append(line[2:].rstrip())
# Close the file
f.close()

# Global variable for holding all events in pygame
gEvent = 0

# List containing timings for movie
timing1 = ["11:00am", "1:30pm", "3:00pm", "5:00pm", "9:00pm"]
# List containing text objects for timings
timing1Text = []
# List containing rectangle objects for timnings
timing1Rect = []


# List containing timings for movie
timing2 = ["11:45am", "1:35pm", "4:00pm", "6:25pm", "8:15pm"]
# List containing text objects for timings
timing2Text = []
# List containing rectangle objects for timnings
timing2Rect = []


# List containing timings for movie
timing3 = ["10:45am", "2:55pm", "4:10pm", "7:25pm", "10:55pm"]
# List containing text objects for timings
timing3Text = []
# List containing rectangle objects for timnings
timing3Rect = []


# List containing timings for movie
timing4 = ["9:35am", "1:10pm", "2:55pm", "7:45pm", "11:05pm"]
# List containing text objects for timings
timing4Text = []
# List containing rectangle objects for timnings
timing4Rect = []


# List containing timings for movie
timing5 = ["11:55am", "3:10pm", "5:25pm", "9:15pm", "11:30pm"]
# List containing text objects for timings
timing5Text = []
# List containing rectangle objects for timnings
timing5Rect = []

# List containing all timings lists
allTimingsTime = [timing1, timing2, timing3, timing4, timing5]
# List containing all timing text object lists
allTimingsText = [timing1Text, timing2Text, timing3Text, timing4Text, timing5Text]
# List containing all timing rectangle lists
allTimingsRect = [timing1Rect, timing2Rect, timing3Rect, timing4Rect, timing5Rect]

# List containing selected seats
seats = [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
        ]
# List containing all taken seats
takenSeat = [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [True, False, False, True, False],
        [False, False, False, True, False],
        [False, False, False, False, False]
        ]
# List containing rectangle objects for seats
seatsRect = [[], [], [], [], []]
# List containing colors for seating
seatsClr = [(72, 165, 234), (2, 59, 102)]

# Variable for ticket number
ticketNumber = None
# Variable for selected movie
selectedMovie = None
# Variable for selected time
selectedTime = None

# Variable for signup username, password, verified password
signupUsername = ''
signupPassword = ''
signupVerifyPassword = ''
# Variables for Paypal username and password
paypalUsername = ''
paypalPassword = ''

# Variables for controlling when to type on specified objects
typeSignupUsername = False
typeSignupPassword = False
typeSignupVerifyPassword = False
typePaypalUsername = False
typePaypalPassword = False

# Variable to control what movie to display
displayIndex = -1
# Variables postioning of movies
displayX = 0
displayY = 0
# Variables controlling when to show seating and payment
showSeating = False
showTiming = False
showPayment = False

# Button function; (x, y) pos of button, (width, height) of the button, clr1: default color of button, clr2: color when button is clicked, event the function uses
def button(x, y, width, height, clr1, clr2, event):
    # Global variables
    global mouseBuffer
    # rectangle with at pos (x, y) and with width and height
    rect = pygame.Rect(x, y, width, height)
    # Drop shadow with pos (x, y) and with width and height
    shadow = pygame.Rect(x, y, width, height)
    # Positioning drop shadow
    shadow.x = center(x, width+5, width)
    shadow.y = center(y, height+5, height)

    # draw rectangle
    pygame.draw.rect(screen, (150, 105, 0), shadow)
    pygame.draw.rect(screen, clr1, rect)

    # check if the event type is the mouse button down (left click)
    if (event.type == pygame.MOUSEBUTTONDOWN):

        # if the position of the mouse collides with button
        if (rect.collidepoint(event.pos) and mouseBuffer):
            # Setting the buffer to false
            mouseBuffer = False
            # draw the rectangle with new color
            pygame.draw.rect(screen, clr2, rect)

            # return true as the button is clicked on
            return True
        else:

            # return false as the button is not clicked on
            return False

# Ticket id creation function, returns a random ticketId
def createTicketId():
    # Characters for the ticket Id
    ticketNumber = "123456789ABCDEFGIH"
    # Variable to hold id
    id =''
    # For loop for character in id
    for i in range (18):
        # Select a random character for id
        id += ticketNumber[random.randrange(0, 18, 1)]
    # return id
    return id
# Set the ticket id
ticketId = createTicketId()

# inputBox, text: text for the input box, event: event used for function, (x, y): x and y coords of input box, (width, height): width and height of input box, font: font used for the input box, (clr1, clr2): color used for box and text, active: variable to check if you can write in the box
def inputBox(text, event, x, y, width, height, font, clr1, clr2, active, isPass):
    global inputBuffer, keyBuffer
    # create the rectangle for display box
    displayBox = pygame.Rect(x, y, width, height)

    # create drop shadow for display box
    shadow = pygame.Rect(x, y, width, height)
    # Postioning drop shadow
    shadow.x = center(x, width+5, width)
    shadow.y = center(y, height+5, height)
    # Draw drop shadow
    pygame.draw.rect(screen, (0,0,0), shadow)
    
    # If the input box is active
    if active:
        # Draw the active input box
        pygame.draw.rect(screen, (150, 150, 150), displayBox)
    else:
        # Draw the inactive input box
        pygame.draw.rect(screen, clr1, displayBox)
    
    # If the input box is a password
    if (isPass):
        # Variable for characters to display
        display = ''

        # For loop for length of input
        for char in range (len(text)):
            # Add '*' to display
            display+='*'
        # Create text for input box
        inputText = font.render(display, True, clr2)

    # Else it is not a password
    else:
        # Create text for input box
        inputText = font.render(text, True, clr2)

    # Get the rect from the text
    inputTextRect = inputText.get_rect()

    # Set the x and y of the text
    inputTextRect.x = x
    inputTextRect.y = y

    # Sisplay the text
    screen.blit(inputText, inputTextRect)

    # if the event type is mouse button down (if the left mouse button is pressed)
    if event.type == pygame.MOUSEBUTTONDOWN:
        # if the mouse position is colliding with the display box
        if (displayBox.collidepoint(event.pos) and inputBuffer):
            # Set the input buffer to false
            inputBuffer = False

            # swap active (if it is false make it true, visa versa)
            active = not active
        # If the inptut box is not clicked on 
        elif (not displayBox.collidepoint(event.pos)):
            # set active to false if the mouse does not collide with the display box
            active = False

    # if the event type is keydown (any key is pressed)
    if event.type == pygame.KEYDOWN and keyBuffer:

        # if the input box is active
        if active:
            # Set the key bufer to false
            keyBuffer = False
            # if the key is the backspace
            if event.key == pygame.K_BACKSPACE:
                # remove the last character
                text = text[:-1]
            # if the key is return
            elif event.key == pygame.K_RETURN:
                # reset the text
                text = ''
            else:
                # else add the key to the current text
                if (len(text) <= 25):
                    # Add the key to current texrt
                    text += event.unicode

    # return the modified text,and active variables
    return text, active

# Login screen function to display the login screen
def loginScreen():
    # Global variables
    global username, typeUsername, gEvent, password, typePassword, currentPage, usernames, passwords
    # Colors for objects
    clr = (5, 132, 230)
    borderClr = (31, 158, 255)
    
    # Position of login screen
    loginX = width/2-400/2
    loginY = height/2-300
    # Draw the border, drop shadow and frame of login screen
    pygame.draw.rect(screen, (2, 87, 153), pygame.Rect(
        center(loginX, 405, 400), center(loginY, 305, 300), 400, 300))
    pygame.draw.rect(screen, clr, pygame.Rect(loginX, loginY, 400, 300))
    pygame.draw.rect(screen, borderClr, pygame.Rect(loginX, loginY, 400, 50))
    # Set up font to be used
    font = pygame.font.Font("Horta demo.otf", 25)
    # Render the font
    title = font.render("LOG-IN", True, (0, 0, 0))
    # Get the rectangle
    titleRect = title.get_rect()
    # Position the object
    titleRect.x = center(loginX, 400, titleRect.width)
    titleRect.y = center(loginY, 50, titleRect.height)
    # display the text
    screen.blit(title, titleRect)
   

    # Render the font
    usernameTitle = font.render("Username", True, (255, 255, 255))
    # Get the rectangle
    usernameTitleRect = usernameTitle.get_rect()
    # Position the object
    usernameTitleRect.x = loginX+15
    usernameTitleRect.y = loginY+50
    # display the text
    screen.blit(usernameTitle, usernameTitleRect)

    # Render the font
    passwordTitle = font.render("Password", True, (255, 255, 255))
    # Get the rectangle
    passwordTitleRect = passwordTitle.get_rect()
    # Position the object
    passwordTitleRect.x = loginX+15
    passwordTitleRect.y = loginY+130
    # display the text
    screen.blit(passwordTitle, passwordTitleRect)

    # Input boxes for username and passwords
    username, typeUsername = inputBox(username, gEvent, loginX+400/2-350/2,
                                      loginY+80, 350, 30, font, (205, 205, 205), (0, 0, 0), typeUsername, False)
    password, typePassword = inputBox(password, gEvent, loginX+400/2-350/2,
                                      loginY+160, 350, 30, font, (205, 205, 205), (0, 0, 0), typePassword, True)
  

    # Render the font
    btn1Title = font.render("Submit", True, (255, 255, 255))
    # Get the rectangle
    btn1TitleRect = btn1Title.get_rect()
    # Position the object
    btn1TitleRect.x = center(loginX+400/2-100/2, 100, btn1TitleRect.width)
    btn1TitleRect.y = center(loginY+210, 50, btn1TitleRect.height)
    # Create button for submitting username and password
    btn1 = button(loginX+400/2-100/2, loginY+210, 100,
                  50, (230, 140, 5), (153, 92, 0), gEvent)
    # Display the text
    screen.blit(btn1Title, btn1TitleRect)

    # If the button has been clicked on 
    if (btn1):
        # If the username and password is correct
        if (username in usernames and password in passwords):
            # Set the current page to the next page
            currentPage = 1
            # Set the mouse position to 0, 0
            pygame.mouse.set_pos(0,0)
        # If the username or password is incorrect
        else:
            # Display issue to user
            tooltip("Username or password incorrect.", 1000)

# Welcome user function that display a welcome to the user
def welcomeUser():
    # Global variables
    global iconImg, iconImgRect, username
    # Set the font to user
    welcomeFont = pygame.font.Font("Horta demo.otf", 30);
    # Render the text
    welcomeText = welcomeFont.render("Welcome, %s"%(username), True, (255,255,255))
    # Get the rectangle
    welcomeTextRect = welcomeText.get_rect()
    # Position the text
    welcomeTextRect.x = width-welcomeTextRect.width-41;
    welcomeTextRect.y = 5

    # Display the welcome text and icon
    screen.blit(welcomeText, welcomeTextRect)
    screen.blit(iconImg, iconImgRect)

# Signup screen function to display the signup screen
def signupScreen():
    # Global variables
    global signupUsername, signupPassword, signupVerifyPassword, typeSignupUsername, typeSignupPassword, typeSignupVerifyPassword, showSignin, showLogin, usernames, passwords
    # Position of login screen
    signinX = width/2-400/2
    signinY = height/2-300

    # Colors for objects
    clr = (5, 132, 230)
    borderClr = (31, 158, 255)

    # Rectangle object for border
    borderRect = pygame.Rect(signinX, signinY, 400, 50)

    # Draw the border, drop shadow and frame of login screen
    pygame.draw.rect(screen, (2, 87, 153), pygame.Rect(
        center(signinX, 405, 400), center(signinY, 355, 350), 400, 350))
    pygame.draw.rect(screen, clr, pygame.Rect(signinX, signinY, 400, 350))
    pygame.draw.rect(screen, borderClr, borderRect)


    # Set up font to be used
    font = pygame.font.Font("Horta demo.otf", 25)
    # Render the font
    title = font.render("SIGNUP", True, (0, 0, 0))
    # Get the rectangle
    titleRect = title.get_rect()
    # Position the object
    titleRect.x = center(signinX, 400, titleRect.width)
    titleRect.y = center(signinY, 50, titleRect.height)
    # display the text
    screen.blit(title, titleRect)

    # Render the font
    usernameTitle = font.render("Enter A Username", True, (255, 255, 255))
    # Get the rectangle
    usernameTitleRect = usernameTitle.get_rect()
    # Position the object
    usernameTitleRect.x = signinX+15
    usernameTitleRect.y = signinY+50
    # display the text
    screen.blit(usernameTitle, usernameTitleRect)

    # Render the font
    passwordTitle = font.render("Enter A Password", True, (255, 255, 255))
    # Get the rectangle
    passwordTitleRect = passwordTitle.get_rect()
    # Position the object
    passwordTitleRect.x = signinX+15
    passwordTitleRect.y = signinY+120
    # display the text
    screen.blit(passwordTitle, passwordTitleRect)

    # Render the font
    passwordVerifyTitle = font.render("Retype Password", True, (255, 255, 255))
    # Get the rectangle
    passwordVerifyTitleRect = passwordVerifyTitle.get_rect()
    # Position the object
    passwordVerifyTitleRect.x = signinX+15
    passwordVerifyTitleRect.y = signinY+190
    # display the text
    screen.blit(passwordVerifyTitle, passwordVerifyTitleRect)

    # Input boxes for signup username, password, and verified password
    signupUsername, typeSignupUsername = inputBox(signupUsername, gEvent, center(
        signinX, 400, 350), signinY+80, 350, 30, font, (205, 205, 205), (0, 0, 0), typeSignupUsername, False)
    signupPassword, typeSignupPassword = inputBox(signupPassword, gEvent, center(
        signinX, 400, 350), signinY+150, 350, 30, font, (205, 205, 205), (0, 0, 0), typeSignupPassword, True) 
    signupVerifyPassword, typeSignupVerifyPassword = inputBox(signupVerifyPassword, gEvent, center(
        signinX, 400, 350), signinY+220, 350, 30, font, (205, 205, 205), (0, 0, 0), typeSignupVerifyPassword, True)

    # Render the font
    submitText = font.render("Submit", True, (255, 255, 255))
    # Get the rectangle
    submitTextRect = submitText.get_rect()
    # Position the object
    submitTextRect.x = center(signinX+400/2-100/2, 100, submitTextRect.width)
    submitTextRect.y = center(signinY+260, 50, submitTextRect.height)

    # Create button for signup 
    submitBtn = button(center(signinX, 400, 100), signinY +
                       260, 100, 50, (230, 140, 5), (153, 92, 0), gEvent)

    # Display the text
    screen.blit(submitText, submitTextRect)
    # If the button has been clicked on 
    if (submitBtn):
        # If the signup password and the verified password are the same, and they are not empty
        if (signupPassword == signupVerifyPassword and signupPassword != '' and signupUsername != ''):
            # Show the login for the user
            showLogin = True
            # Stop showing the signup screen
            showSignin = False
            # Open the loginInfo text file
            f = open("loginInfo.txt", "a")
            # Add the username and password to file
            f.write("\nu %s\n" %(signupUsername))
            f.write("p %s\n" %(signupPassword))
            # Close the file
            f.close()
            # Add the username and password to the lists
            usernames.append(signupUsername)
            passwords.append(signupPassword)
        # If the signup password is empty
        elif (signupPassword == ''):
            # Display issue to user
            tooltip("Password cannot be empty.", 1000)
        # If the singup username is empty
        elif (signupUsername ==''):
            # Display issue to user
            tooltip("Username cannot be empty.", 1000)
        else:
            # Display issue to user
            tooltip("Passwords do not match.", 1000)

# Login button function that display the sign up and login buttons
def loginButtons():
    # Global variables
    global mouseBuffer, showLogin, showSignin
    # Color of login buttons
    loginBtnClr = (255, 255, 255)
    # Set up font to use
    loginBtnFont = pygame.font.Font("Horta demo.otf", 30)
    # Render the login buttons as text
    loginBtn = loginBtnFont.render("Log-in", True, loginBtnClr)
    signBtn = loginBtnFont.render("Sign-up", True, loginBtnClr)

    # Positioning login buttons
    loginBtnRect = loginBtn.get_rect()
    loginBtnRect.x = width-100-loginBtnRect.width/2
    signBtnRect = signBtn.get_rect()
    signBtnRect.x = width-200-signBtnRect.width/2
    # Display login buttons
    screen.blit(loginBtn, loginBtnRect)
    screen.blit(signBtn, signBtnRect)

    # If the mouse buffer is clear and the login button is clicked on
    if (mouseBuffer and loginBtnRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
        # Swap showing the login screen
        showLogin = not showLogin
        # Set the mouse buffer to false
        mouseBuffer = False
        # Stop showing the signup screen
        showSignin = False
    # If the mouse bugger is clear the signup button is clicked on
    if (mouseBuffer and signBtnRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
        # Swap showing the signup screen
        showSignin = not showSignin
        # Set the mouse buffer to false
        mouseBuffer = False
        # Stop showing the login screen
        showLogin = False
    # If showLogin is true, show the login screen
    if (showLogin):
        loginScreen()

    # If showSignin is true, show the signup screen
    if (showSignin):
        signupScreen()

# Login page function that displays the login page
def loginPage():
    # Fill the screen with the background color
    screen.fill(bkgClr)
    # Draw a border for the screen
    pygame.draw.rect(screen, (barClr), pygame.Rect(0, 0, width, 50))
    # Draw image designs to screen
    screen.blit(logo, logoRect)
    screen.blit(acct, acctRect)
    screen.blit(cinemaImg, cinemaImgRect)
    screen.blit(arrowImg, arrowImgRect)
    # Show login buttons
    loginButtons()

# Instructions function that displays what the user should do next
def instructions(text, offsetX, offsetY):
    # Set up color
    instructClr = (255, 255, 255)
    # Set up font
    instructFont = pygame.font.Font('Horta demo.otf', 40)
    # Render the title with font
    instructTitle = instructFont.render(text, True, instructClr)
    # Get rectangle
    instructTitleRect = instructTitle.get_rect()
    # Positioning the rectangle
    instructTitleRect.x = center(offsetX, width, instructTitleRect.width)
    instructTitleRect.y = offsetY
    # Draw the title to the screen
    screen.blit(instructTitle, instructTitleRect)

# Movie page function that shows the movie page
def moviePage():
    # Global variables
    global gEvent, displayIndex, displayX, displayY, showSeating, selectedMovie, movies, showPayment, mouseBuffer, showTiming
    # Fill the screen with background color
    screen.fill(bkgClr)
    # Draw the dar
    pygame.draw.rect(screen, (barClr), pygame.Rect(0, 0, width, 50))
    # Set the color
    logoClr = (40, 255, 13)
    nowShowClr = (212, 136, 13)
    godzillaTitleClr = (255, 255, 255)
    spidermanTitleClr = (255, 255, 255)
    avengersTitleClr = (255, 255, 255)
    interstellarTitleClr = (255, 255, 255)
    inceptionTitleClr = (255, 255, 255)

    # Set the font 
    logoFont = pygame.font.Font("Horta demo.otf", 40)
    godzillaTitleFont = pygame.font.Font('Horta demo.otf', 30)
    spidermanTitleFont = pygame.font.Font('Horta demo.otf', 30)
    avengersTitleFont = pygame.font.Font('Horta demo.otf', 30)
    interstellarTitleFont = pygame.font.Font('Horta demo.otf', 30)
    inceptionTitleFont = pygame.font.Font('Horta demo.otf', 30)
    nowShowFont = pygame.font.Font('Horta demo.otf', 42)

    # Render the font
    logo = logoFont.render("MOVIEFLEX", True, logoClr)
    godzillaTitle = godzillaTitleFont.render('Godzilla vs Kong', True, godzillaTitleClr)
    spidermanTitle = spidermanTitleFont.render('Spider-Man 3', True, spidermanTitleClr)
    avengersTitle = avengersTitleFont.render('Avengers: Infinty War', True, avengersTitleClr)
    interstellarTitle = interstellarTitleFont.render('Interstellar', True, interstellarTitleClr)
    inceptionTitle = inceptionTitleFont.render('Inception', True, inceptionTitleClr)
    nowShow = nowShowFont.render('Now Showing', True, nowShowClr)

    # Get the rectangle
    logoRect = logo.get_rect()
    godzillaTitleRect = godzillaTitle.get_rect()
    spidermanTitleRect = spidermanTitle.get_rect()
    avengersTitleRect = avengersTitle.get_rect()
    interstellarTitleRect = interstellarTitle.get_rect()
    inceptionTitleRect = inceptionTitle.get_rect()
    nowShowRect = nowShow.get_rect()

    # Positioning the text
    logoRect.x = (width/2-625)
    logoRect.y += 0.5
    nowShowRect.x = width/2-620
    nowShowRect.y += 90
    godzillaTitleRect.x = width/2-590
    godzillaTitleRect.y += 675
    spidermanTitleRect.x = width/2-320
    spidermanTitleRect.y += 675
    avengersTitleRect.x = width/2-110
    avengersTitleRect.y += 675
    interstellarTitleRect.x = width/2-(-180)
    interstellarTitleRect.y += 675
    inceptionTitleRect.x = width/2-(-450)
    inceptionTitleRect.y += 675

    # Display text to screen
    screen.blit(nowShow, nowShowRect)
    screen.blit(godzillaTitle, godzillaTitleRect)
    screen.blit(spidermanTitle, spidermanTitleRect)
    screen.blit(avengersTitle, avengersTitleRect)
    screen.blit(interstellarTitle, interstellarTitleRect)
    screen.blit(inceptionTitle, inceptionTitleRect)
    screen.blit(logo, logoRect)

    # Display welcome to the user
    welcomeUser()

    # For loop to display movie pictures
    for i in range (5):
        # Display movie to screen
        screen.blit(movieImg[i], movieRect[i])

    # For loop to check if the movies have been clicked on
    for i in range (5):
        # If the event is the mouse has been clicked
        if (gEvent.type == pygame.MOUSEBUTTONDOWN):
            # If the movie poster has been clicked on, and no other screens are being shown
            if movieRect[i].collidepoint(gEvent.pos) and not showSeating and not showPayment:
                # Set position of the next screen
                displayX = center(movieRect[i].x, movieRect[i].width, 400);
                displayY = 70
                # Set the display index to selected movie
                displayIndex = i
                # Stop showing the seating
                showSeating = False
                # Show timing
                showTiming = True
                # Change the selected movie
                selectedMovie = movies[i]
                # If it is the first movie
                if (i == 0):
                    # Change the position
                    displayX = 5
                # Elif it is the last movie
                elif (i==4):
                    # Change the position
                    displayX = width-480

    # If the displayindex is not equal to -1 
    if displayIndex != -1:
        # If the seating is not being shown and the payment is not being shown
        if (showTiming == True and not showPayment):
            # Give instructions to user
            instructions("Select a Time", 0, 1)
            # Display the timing
            showTiming = timing(displayX, displayY, displayIndex)
    # Else give instructions to user
    else:
        instructions("Click on a Movie to select", 0, 1)
    
    # If the seating window is being shown
    if showSeating:
        # Stop showing the payment
        showPayment = False
        # Stop showing timing
        showTiming = False
        # Show the seatings
        showSeating = seatings(displayX, displayY)
        # Give instructions to user
        instructions("Select seats you want", 0, 1)
    # If the payment window is being shown
    if showPayment:
        # Stop showing the seating
        showSeating = False
        # Stop showing timing
        showTiming = False
        # Give instructions to user
        instructions("Add your PayPal details", 0, 1)
        # Show the payment screen
        showPayment = payment(displayX, displayY)   

# Ticket page function that shows the ticket page
def ticketPage():
    # Global
    global ticketNumber, selectedMovie, ticketId, selectedTime
    # Setup color
    thankClr = (255, 215, 0)
    # Set up the fonts
    font = pygame.font.Font("Horta demo.otf", 100)
    font1 = pygame.font.Font("Horta demo.otf", 60)
    # Render the text
    thank = font.render("Thank You for Your Order!", True, thankClr)
    selectedMovieText = font1.render("Selected Movie: "+str(selectedMovie), True, (255,255,255))
    ticketNumberText = font1.render("Total amount of tickets: " + str(ticketNumber), True, (255,255,255))
    totalPriceText = font1.render("Final Price: $%.2f" % (10.99*ticketNumber), True, (255,255,255))
    ticketIdText = font1.render("Ticket ID: %s" %(ticketId), True, (255,255,255) )
    timeText = font1.render("Time: %s" %(selectedTime), True, (255,255,255) )
    # Get the rectangle
    thankRect = thank.get_rect()
    selectedMovieTextRect = selectedMovieText.get_rect()
    ticketNumberTextRect = ticketNumberText.get_rect()
    totalPriceTextRect = totalPriceText.get_rect()
    ticketIdTextRect = ticketIdText.get_rect()
    timeTextRect = timeText.get_rect()
    # Positioning the text
    thankRect.x = (width/2-400)
    thankRect.y += 120
    selectedMovieTextRect.x = center(0, width, selectedMovieTextRect.width)
    selectedMovieTextRect.y = 250
    ticketNumberTextRect.x = center(0, width, ticketNumberTextRect.width)
    ticketNumberTextRect.y = 300
    totalPriceTextRect.x = center(0, width, totalPriceTextRect.width)
    totalPriceTextRect.y = 350
    ticketIdTextRect.x = center(0, width, ticketIdTextRect.width)
    ticketIdTextRect.y = 450
    timeTextRect.x = center(0, width, timeTextRect.width)
    timeTextRect.y = 400
    # Display the welcome to the user
    welcomeUser()
    # Fill the screen with the background color
    screen.fill(bkgClr)
    # Draw the bar for the screen
    pygame.draw.rect(screen, (barClr), pygame.Rect(0, 0, width, 50))
    # Draw the images for the screen
    screen.blit(logo, logoRect)
    screen.blit(cinemaImg, cinemaImgRect)
    # Display the text
    screen.blit(thank, thankRect)
    screen.blit(selectedMovieText, selectedMovieTextRect)
    screen.blit(ticketNumberText, ticketNumberTextRect)
    screen.blit(totalPriceText, totalPriceTextRect)
    screen.blit(ticketIdText, ticketIdTextRect)
    screen.blit(timeText, timeTextRect)

# Timing function that shows the timing for each movie
def timing(offsetX, offsetY, timeIndex):
    # Global variables
    global timing1, allTimingsRect, allTimingsText, allTimingsTime, gEvent, selectedTime, allTimingsTime, mouseBuffer, showTiming, showSeating
    # Set up colors
    clr = (5, 132, 230)
    borderClr = (31, 158, 255)
    # Set up font
    font = pygame.font.Font("Horta demo.otf", 40)
    # Draw the window and drop shadow
    pygame.draw.rect(screen, (2, 87, 153), pygame.Rect(center(offsetX, 405, 400), center(offsetY, 255, 250), 400, 250))
    pygame.draw.rect(screen, clr, pygame.Rect(offsetX, offsetY, 400, 250))
    if (gEvent.type == pygame.MOUSEBUTTONUP):
        mouseBuffer=True
    
    # For loop to render the timings
    for i in range(5):
        # Create rectangle
        rect = pygame.Rect(offsetX, offsetY+(i*50), 400, 50)
        # Draw the rectangle to the screen
        pygame.draw.rect(screen, borderClr, rect)
        # Append the rectangle to the timing rectangle list
        allTimingsRect[timeIndex].append(rect)
        # Render the text for timing
        text = font.render(allTimingsTime[timeIndex][i], True, (255,255,255))
        # Add the text to the timing text list
        allTimingsText[timeIndex].append(text)
    # If the mouse is clicked
    if gEvent.type == pygame.MOUSEBUTTONUP:
        # For loop checking if the timing has been selected
        for i in range(5):
            # If the timing clikced on
            if (allTimingsRect[timeIndex][i].collidepoint(pygame.mouse.get_pos())):
                # Set mouse buffer to false
                mouseBuffer = False
                # Draw the timing box
                pygame.draw.rect(screen, clr, allTimingsRect[timeIndex][i])
                # Set the selected time
                selectedTime = allTimingsTime[timeIndex][i]
                # Return true for the function
                showTiming = False
                showSeating = True
    # For loop to draw the dividers and draw the text
    for i in range(5):
        # Draw the divider for the time
        pygame.draw.line(screen, (2, 87, 153), (offsetX, offsetY+50+i*50), (offsetX+400, offsetY+50+i*50))
        # Display the timing text to the screen
        screen.blit(allTimingsText[timeIndex][i], allTimingsRect[timeIndex][i])
    # Clear the rectangle list
    allTimingsRect[timeIndex].clear()
    # Return true
    return True
# Seating function that shows the seating for each movie
def seatings (offsetX, offsetY):
    # Global variables
    global seatsRect, seatsClr, seats, gEvent, mouseBuffer, ticketNumber, currentPage, takenSeat, showPayment
    # Set up colors
    clr = (5, 132, 230)
    borderClr = (31, 158, 255)
    # Set up font
    font = pygame.font.Font("Horta demo.otf", 40)
    # Create rectangle for frame
    frame = pygame.Rect(offsetX, offsetY, 475, 250)
    # Draw the window and frame
    pygame.draw.rect(screen, (2, 87, 153), pygame.Rect(center(offsetX, 480, 475), center(offsetY, 255, 250), 475, 250))
    pygame.draw.rect(screen, clr, frame)
    
    # Set the padding for the seatings
    padding = 5
    # Set the seating width and height
    seatWidth = (400-((padding+1)*5))/5
    seatHeight = (250-((padding+1)*5))/5

    # If the mouse button is clicked
    if (gEvent.type == pygame.MOUSEBUTTONDOWN):
        # If the mouse is not clicking on the frame
        if (not frame.collidepoint(gEvent.pos)):
            # Return false
            return False
    # For loop for each row of seatings
    for i in range (5):
        # For loop for each column of seatings
        for j in range (5):
            # Create the rectangle for seat
            rect = pygame.Rect(offsetX + i*seatWidth + padding*(i+1), offsetY + j*seatHeight + padding*(j+1), seatWidth, seatHeight)
            # If the seat is selected
            if (seats[i][j] and not takenSeat[i][j]):
                # Draw the seat
                pygame.draw.rect(screen, seatsClr[1], rect)
            # If the seat is taken
            elif (takenSeat[i][j]):
                # Draw the seat
                pygame.draw.rect (screen, (255,0,0), rect)
            else:
                # Draw the seat
                pygame.draw.rect(screen, seatsClr[0], rect)
            # Append the seating to the seating rectangle list
            seatsRect[i].append(rect)
    # For loop for each row in seatings
    for i in range (5):
        # For loop for each column in seatings
        for j in range (5):
            # If the mouse button is clicked on
            if gEvent.type == pygame.MOUSEBUTTONDOWN:
                # If the seat that is clicked on is not taken
                if seatsRect[i][j].collidepoint(gEvent.pos) and not takenSeat[i][j] and mouseBuffer:
                    # Set the mouse buffer to false
                    mouseBuffer = False
                    # Swap the availablity of the seat
                    seats[i][j] = not seats[i][j]
    # For loop for each row in seatings
    for i in range(5):
        # Clear the seatings
        seatsRect[i].clear()

    # Variable controlling when to show the submit button
    showButton = False
    # For loop for each row in seatings
    for i in range (5):
        # For loop for each column in seatings
        for j in range(5):
            # If any of the seats have been selected
            if seats[i][j]:
                # Show the button
                showButton = True
    # If the button is showing
    if showButton:
        # Create the button
        btn = button(offsetX+ 5*seatWidth + (6*padding), offsetY+padding, 70, 240, (230, 140, 5), (153, 92, 0), gEvent)
        # If the button has been clicked on
        if btn:
            # Variable to check how many tickets bought
            tickets = 0
            # For loop for each row in seatings
            for i in range (5):
                # For loop for each column in seatings
                for j in range(5):
                    # If the seat is selected
                    if seats[i][j]:
                        # Add to the total amount of tickets
                        tickets+=1
            # Set the ticket number
            ticketNumber = tickets
            # Show the payment screen
            showPayment = True
    # Return true
    return True

# Payment function that show the payment screen for selected movie
def payment (offsetX, offsetY):
    # Global variables
    global paypalUsername, paypalPassword, typePaypalPassword, typePaypalUsername, gEvent, currentPage, ticketNumber
    # Set up colors
    clr = (5, 132, 230)
    borderClr = (31, 158, 255)
    # Set up fonts
    font = pygame.font.Font("Horta demo.otf", 40)
    font2 = pygame.font.Font("Horta demo.otf", 25)
    
    # Draw the screen, border, and drop shadow
    pygame.draw.rect(screen, (2, 87, 153), pygame.Rect(center(offsetX, 405, 400), center(offsetY, 255, 250), 400, 250))
    pygame.draw.rect(screen, clr, pygame.Rect(offsetX, offsetY, 400, 250))
    pygame.draw.rect(screen, borderClr, pygame.Rect(offsetX, offsetY, 400, 50))
    
    # Render the font
    title = font.render("Cost of Tickets: $%.2f" %(10.99*ticketNumber),True, (255,255,255))
    paypalUsernameText = font2.render("Enter PayPal email", True, (255,255,255))
    paypalPasswordText = font2.render("Enter PayPal password", True, (255,255,255))
    btn1Title = font2.render("Submit", True, (255, 255, 255))
    # Get the rectangle
    titleRect = title.get_rect()
    paypalUsernameTextRect = paypalUsernameText.get_rect()
    paypalPasswordTextRect = paypalPasswordText.get_rect()
    btn1TitleRect = btn1Title.get_rect()
    # Positioning the text
    titleRect.x = center(offsetX, 400, titleRect.width)
    titleRect.y = offsetY
    paypalUsernameTextRect.x = offsetX+10
    paypalUsernameTextRect.y = offsetY+50
    paypalPasswordTextRect.x = offsetX+10
    paypalPasswordTextRect.y = offsetY+130
    btn1TitleRect.x = center(offsetX+400/2-100/2, 100, btn1TitleRect.width)
    btn1TitleRect.y = center(offsetY+197, 50, btn1TitleRect.height)
    # Display the text
    screen.blit(title, titleRect)
    screen.blit(paypalUsernameText, paypalUsernameTextRect)
    screen.blit(paypalPasswordText, paypalPasswordTextRect)

    # Input boxes for Paypal email and password
    paypalUsername, typePaypalUsername = inputBox(paypalUsername, gEvent, center(
        offsetX, 400, 350), offsetY+80, 350, 30, font2, (205, 205, 205), (0, 0, 0), typePaypalUsername, False)
    paypalPassword, typePaypalPassword = inputBox(paypalPassword, gEvent, center(
        offsetX, 400, 350), offsetY+160, 350, 30, font2, (205, 205, 205), (0, 0, 0), typePaypalPassword, True)

    # Create button to submit Paypal details
    btn1 = button(offsetX+400/2-100/2, offsetY+197, 100,
                  50, (230, 140, 5), (153, 92, 0), gEvent)

    # If the button is clicked on
    if(btn1):
        # If the Paypal email has '@' symbol and the password is not blank
        if ("@" in paypalUsername and paypalPassword != ''):
            # Move to the final page
            currentPage = 2
        # If the email is invaild
        elif (not "@" in paypalUsername):
            # Display issue to user
            tooltip("Invalid email address. (missing '@')", 1000)
        # If the password is empty
        elif (paypalPassword == ''):
            # Display issue to user
            tooltip("Password cannot be empty.", 1000)
    # Display the text for button
    screen.blit(btn1Title, btn1TitleRect)
    # Return true
    return True

# Tooltip function that shows what is wrong 
def tooltip (text, time):
    # Set up font
    font = pygame.font.Font("Horta demo.otf", 25)
    # Create rectangle for display box
    displayBox = pygame.Rect(0,0,width-50, 40)
    # Render the text
    toolText = font.render(text, True, (255,255,255))
    # Get the rectangle
    toolTextRect = toolText.get_rect()
    # Positioning text
    toolTextRect.x = center(0, width, toolTextRect.width)
    toolTextRect.y = center(0, height, toolTextRect.height)
    displayBox.x = center(0, width, displayBox.width)
    displayBox.y = center(0, height, displayBox.height)

    # Draw the displaybox
    pygame.draw.rect(screen, (160,160,160), displayBox)
    # Display the text
    screen.blit(toolText, toolTextRect)
    # Update the screen
    pygame.display.flip()
    # Wait for specified time
    pygame.time.wait(time)

# Variable to hold current page
currentPage = 0
# Pygame clock to control speed of program
clock = pygame.time.Clock()
# While true loop for program
while True:
    # Polling all events in pygame
    for event in pygame.event.get():
        # Set the event 
        gEvent = event
        # If user closes the window
        if event.type == pygame.QUIT:
            # Close python
            sys.exit()
        # If any key is released
        if event.type == pygame.KEYUP:
            # Clear the key buffer
            keyBuffer = True
        # If the mouse button is released
        if event.type == pygame.MOUSEBUTTONUP:
            # Clear the mouse buffer and input buffer
            mouseBuffer = True
            inputBuffer = True
        # Set pygame's speed to 90 ticks
        clock.tick(90)

    

    # If it is the first page
    if (currentPage == 0):
        # Display login page
        loginPage()
    # If it is the second page
    elif (currentPage ==1):
        # Display movie page
        moviePage()
    # If it is the third page
    elif(currentPage ==2):
        # Display the ticket page
        ticketPage()
    # Update the screen
    pygame.display.flip()