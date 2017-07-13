name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Conversion logic
height_in_cm = height * 2.54
weight_in_kg = weight * 0.45359237

# Python format characters
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % height_in_cm
print "He's %d pounds heavy." % weight
print "He's %f kgs heavy." % round(weight_in_kg, 2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# Use %r as wildcard for print this, no matter what
# %r for debugging since it displays the "raw" data of the variable

# this line is tricky, try and get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
