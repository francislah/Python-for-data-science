ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

ft_list[1] = "World!"
print(ft_list)

tmp_list = list(ft_tuple)
tmp_list[1] = "Canada"
ft_tuple = tuple(tmp_list)
print(ft_tuple)

# Arbitrarily ordered
ft_set.discard("tutu!")
ft_set.add("Quebec")
print(ft_set)

ft_dict.update({"Hello":"42Quebec"})
print(ft_dict)
