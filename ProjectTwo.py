#Section 1
    #1. In means of adding reading and writing functionality one way would be to create a mthod that allows us to work out these files.
# Depending on what information we as programmers are wanting and/or allowing on a file would affect the details of the method. The method could operate by ensuring a file is being opened by a certain name.
#In said file, in our project one example, details of our objects being made would be written/saved to such file. Examples being a car's label, miles, gas tank, and year.

    #2. My understanding of these so far is that they work similar to their titles. In 'try' we write for the code to /try/ something.
#Such as getting a string and converting it into an integer. IF said action can not be completed then we move to the except part of the clause. This clause helps us rather than having our program shut down as we can introduce a transition on how to move on with these exceptions.
#If the string was not able to be converted then we could have the user be presented with an error message rather than have the code break or continue inappropriately.
#As for the FileNotFoundError class this is an exception that is raised when a program tries to access a file that doesn't exist.

    #3. One section would be at the beginning of my program. Writing a mthod that has the user open a file to havve the object they make be saved in their. That way it doesn't have to be all done within the main.
#Alternatively could be to have it open a file to read from, so that the user can pull information about said object from the class. And then use that in other methods based on said information.


#Test num.1
"""Another way to rewrite the inputting of the number of pages in the album could be.."""
        invalid_input = True
        while invalid_input:
            try:
                num_pages = int(input("Enter the number of pages in the photobook: "))
                invalid_input = False
            except ValueError:
                print("Your input was not an integer and/or is invalid. Try again")

"""or rewriting the aspect of inputting the name"""
#Test num.2
        invalid_input = True
        while invalid_input:
            try:
                name = input("Enter the name of the album: ")
                if len(name) > 100:
                    print("Name is too  long. Must be less than 100 characters.")
                else:
                    invalid_input = False
            except ValueError:
                print("Invalid input")

--------------------------------------------------------------------------------
#Section 2
#When adding these functions to the previous project, they simply do their job. They detect what I want them to do and state it.
#But ultamitely I believe that they are too simple. Such as they only detect if a certain maximum is reached.
#But another layer that could be added is to also detect exceptions to excusing a large title depending on the size of the package. To be able to determine if the titles too large for different ranges of dimensions.


-------------------------
#Section 3
    #1. When attempting to add files to read into the program I was able to get it to work. As the code itself was not too complex from the start.
#By trying to add the similar code examples we've seen, the code was able to handle opening a file by said filename. But when I continue on to try to have aspects of the code be written into the code, this is where I counter some challenges.
#When trying to get the rounds of areas calculated to the document. Some aspects of the code might have to be adjusted in order to make this happen. The user would be asked for the dimensions but when calculated there were issues that our try and except block was not reading well. As a result, our program would crash.
#.There are some sections that could be made into methods to avoid difficulties when further developing the program.
#The first example is the area calculations. They tried to import functions from math and adding it to the variable self.area. But in my case of wanting to add the areas to a file.
# I personally found it to be better organized if the calculation was done in a method, that can later be called within the try/except clause at the acceptable time.
# Since this program would request 3 inputs, the first 2 are related to the core of the programs intent.
#When entering dimension to get an area of, if the numbers were greater than 1 for both then a correct number would be output. However, when both were 0, we would recieve an error message. But this was intential by the coder. However, if both of the dimensions were 1, the output would be -2041... which is incorrect. Therefore, there are more exceptions needed tgo be considered for this code.
#And in the case if the coder wanted to continue, the code would break regardless if the input was correct or not.
#For the majority of the this example, many of the pycodestyle comments are errors on the syntax. Stating E505 line too large. But also messages such as "expected # blank line" and "over-indented."
#While ideally codes need to be organized and clean, in my opinion points like these are acceptable depening on the situation. For personal and small programs, things like this can be overlooked if the intention of the program is being met.
#But in a professional environement, these would be expected to be cleaned. Similar to how it also is for writers/research papers/etc with grammer and punctuation.

