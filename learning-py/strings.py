website = "https://soumilroy.com is      my site"
print (website)

message = "I'm a programmer"
print (message)

message2 = 'I\'m a programmer'
print (message2)

# Concatenation
print ("Darth" + " " + "Vader")

# Multiplication
meme = "lo"
print (meme * 6)

# String indexes 
name = "Soumil"
print (name[0]);
print (name[1]);
print (name[2]);
print (name[3]);
print (name[4]);
print (name[5]);

print (name[0] + name[3]);

# Slicing strings
message = "Hello Python!"
print (message[6:15]);
print (message[6:-1]);
print (message[-15:-8]) # Slicing from EOS
print (message[4:]) # from index 4 till the end 'o Python!'
print (message[:6]) # from index 0 till 6 'Hello '

# Get characters from EOS
print (name[-1]);
print (name[-2]);

# Index that doesn't exist
# print (name[10]);

# Slicing with steps
print (message[2:10:3]) # 3 being the skip step
print (message[2:15:2]) # skip every 2 chars
# Strings
string = "Hello Python!"
print (string[2:9])
print ("********END OF PROGRAM********")

# Escape characters
# Examples: \n, \t, \b, \r, \f, \v, \", \', \\

print ("Hello \nPython!") # New line
print ("Hello \t\tPython!") # Tab
print ("Hello \bPython!") # Backspace
print ("Hello \rPython!") # Carriage return
print ("Hello \fPython!") # Form feed
print ("Hello \vPython!") # Vertical tab
print ("\"Hello Python!\"") # Double quotes
print ("Hello \\Python!") # Backslash

message = """
	A quick brown fox 
	jumps over the lazy dog.
	Lorem ipsum dolor sit amet, 
	consectetur adipiscing elit.
"""

print (message)

# String length function
print (len(message)) # 107

# print (len(122))
print (len("")) # 0

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")