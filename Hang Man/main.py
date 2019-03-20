import random
import os, time

words = []
file = open('secretwords.txt' , 'r')
words = file.read().splitlines()
secret_word = random.choice(words)

print("---------------------------------------------------------")
print("𝐒 𝐊 𝐑 𝐈 𝐕  𝐁 𝐀 𝐑 𝐀  𝐌 𝐄 𝐃  𝐒 𝐌 Å  𝐁 𝐎 𝐊 𝐒 𝐓 Ä 𝐕 𝐄 𝐑")
print("")
print("")
print("•._.••´¯``•.¸¸.•`𝓗 ä 𝓷 𝓰 𝓪  𝓖 𝓾 𝓫 𝓫 𝓮`•.¸¸.•´´¯`••._.•")
print("")
print("")
print("programmet skrivet av: 𝐿𝓊𝒸𝒶𝓈 𝐵𝒶𝓊𝓃𝓈𝑔𝒶𝒶𝓇𝒹")
print("---------------------------------------------------------")
print("")
print("")

def get_guess():

  # Lägger _ på alla bokstäver i gömda ordet
  # ger spelaren 01 liv
  dashes = "-" * len(secret_word)
  left = len(secret_word)
  guesses_left = 10
  used_letters = []


  # En loop som kollar om du har slut på gissningar eller ifall _ är lika som ordet
  while guesses_left > 0 and not dashes == secret_word:

    # Print the amount of dashes and guesses left
    print(dashes)
    print("Bokstäver gissade: ", (used_letters))
    print ("Liv kvar: ", str(guesses_left))

    # frågar spelaren efter en gissning
    guess = input("Gissa:")
    used_letters.append(guess)

    # Varnar ifall man inte skrivern en bokstav eller om man skriver fler än en bokstav
    if len(guess) != 1:
      print("")
      print ("Din bokstav måste vara en bokstav!")

    # Ifall man gissar rätt så printar den det och sedan byter ut _ till bokstaven
    elif guess in secret_word:
      print("")
      print ("Du gissade en bokstav rätt!")
      dashes = update_dashes(secret_word, dashes, guess)


    # Om spelaren gissar fel så säger programmet det och sedan tar bort ett liv från spelarn
    else:
      print("")
      print ("Du gissade fel.")
      guesses_left -= 1

  if guesses_left < 1:
    print ("Du förlora, ordet var: " + str(secret_word))

  # Om _ är lika som ordet så har spelaren vunnit.
  else:
    print ("Grattis! du fick rätt ord: " + str(secret_word))

# Den här funktionen uppdaterar alla _ genom att byta ut _ med bokstäverna som spelaren gissar. Ifall den gissar rätt bokstav alltså
def update_dashes(secret, cur_dash, rec_guess):
  result = ""

  for i in range(len(secret)):
    if secret[i] == rec_guess:
      # Lägger till liv ifall spelaren gissar rätt bokstav
      result = result + rec_guess

    else:
      # Lägger till _ i resultatet ifall bokstaven inte passar resultatet.
      result = result + cur_dash[i]

  return result

get_guess()
