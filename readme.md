# Cat food
---------------------------------------
Inspired by my two cats, I decided to take a adventure with Open CV and Python to play around with image processing and somehow extract information from.

Basically, it prepare the image uses the Hough Circles algorithm to find the circular dish, from that create a mask with the circle size and uses hue and saturation to distinguish food from dish, take pixel area from it and compare to the initial circle area to present a percentage amount.

Isn't perfect and has a lot of flaws, must be a fixed distance between the camera and the dish, the measure is aproximated and is acceptable because the type of dish is cone shaped so height and width are relatable to fill. 

### Input image vs. Output image

---------------------------------------

<img src="/usecases/0.jpg" alt="Input" width="350"/>
<img src="/examples/a8.jpg" alt="Output" width="350"/>
<img src="/usecases/50.jpg" alt="Input" width="350"/>
<img src="/examples/b8.jpg" alt="Output" width="350"/>

### Video
---------------------------------------
Shows the steps.
[![](https://img.youtube.com/vi/hG0DZGl7BTY/0.jpg)](https://www.youtube.com/watch?v=hG0DZGl7BTY)