### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# card.value in the if statment must have the double '==' operand opposed to the single '=' operand
# and the else statment needs a colon ':' after it

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# highest_card needs to be defined using the 'def' keyword not 'dif'
# there is no comma between the second and third parameters of the function
# the first return statement returns an unknown parameter it should be card1
# the indentation of the if statement needs to be corrected accordingly

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# function needs to be indented from our class
# total has no value assigned to it should be total = 0
# our return statement needs to be inline with the for statement
# return statement will return TypeError as total is not a string
# there should be a space after the of in the return - like so "of "

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
