#def the_youngest_child(*kids): # * gives the opportunity to not set the amount of arguments ask for
    #print("The youngest child is " + kids[-1])

#the_youngest_child("Emil", "Tobias", "Linus", "Tim")



def sample_function(**demographic):
    for k, v in demographic.items():
        print(f"My {k} is {v}")

sample_function(name="Lisa", age=23, starsign="virgo")