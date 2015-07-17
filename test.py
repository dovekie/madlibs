
person = "mary"
color = "teal"
noun = "seagull"
adjective = "splendid"

madlib = "There once was a ~ ~ sitting in the Hackbright Lab. When ~ went to pick it up, it burst into flames in a totally ~ way."
madlib_list = madlib.split("~")
mad_string = madlib_list[0] + person + madlib_list[1] + color + madlib_list[2] + noun 
mad_string = mad_string + madlib_list[3] + adjective + madlib_list[4]

print mad_string