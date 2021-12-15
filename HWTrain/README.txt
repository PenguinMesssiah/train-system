Module Reflection

In lieu of a completely functional module, this document reviews the shortcomings of the HW Train Controller and what I would do differently if I had more time.

Coding Process 
There were 3 main steps in my coding process:

A. Hardware Implementation In order to get a functional controller, I first started with creating a simple breadboard circuit. This involved connecting the GPIO pins on the Pi to pushbuttons on the breadboard that triggeered certain events, such as the emergency brake or altering the speed. I also spent a large amount of time configuring the Pi for tactile input (the WiringPi library), which allowed the buttons to communicate with my software. I also learned a lot about GPIO, as it was my first time connecting the pins to the Pi.

B. Software Backend 
The most time was spent on this section. This included adding a RPi console for the user to interact with and tinkering with PyQt. Ultimately, I was not able to get a PyQt interface to show on the RPi (I was getting an error where the entire PyQt window was transparent and could not be manipulated. To combat this, I quickly drafted a console interface instead that relies on a large if statement structure. This allows variables to still be changed, though in a less visually appeasing way. Technically, this still fulfills the requirement of being run through hardware, but it was frustrating to not have a GUI to show. I would spend more time troubleshooting PyQt in the beginning stages of the project, as it is mostly crucial to getting a clean interface working.

C. Connecting to other modules 
Lastly, I spent the last week of the project fixing and fine-tuning connections. This included sending out hardware inputs to the SW module, and creating all of the connections for the SW module to the rest of the system. I used the PyQt signals library to send and receive signals from HW, MBO, and Train Model. I updated these values in a method in the main class. This is the least complete and fleshed-out part of the project, as it was difficult to test with team members and the least understoof by the entire time.

Had I had more hindsight, I would've set a solid framework to begin with - a PyQt interface that works, and connections to at least 1 module. Then, I would be able to expand upon basics and create a more complex module as the semester went on. Overall, given my team's struggles and my own health struggles in the beginning of the semester, I am very proud of the work we did and grateful for the opportunity to learn about systems engineering.

