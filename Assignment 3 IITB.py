#Create an example on string template class

#eg1.

from string import Template

t = Template('$when, $who $action $what.')
s= t.substitute(when='In the summers', who='i', action='love to wear', what ='shorts')
print(s)
