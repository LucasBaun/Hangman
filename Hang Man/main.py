import random # Importerar att den ska kunna göra random 

words = [] # Nämner ordet "words" så jag kan använda det senare.
file = open('secretwords.txt' , 'r') # öppnar och läses filen secretwords.txt
words = file.read().splitlines() # Säger att den bara ska läsa varje rad som ett objekt.
secret_word = random.choice(words) # Väljer ut ett random ord.

# Printar ut spelet!
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

def get_guess(): # Startar en funktion.

  dashes = "-" * len(secret_word) # Lägger _ på alla bokstäver i gömda ordet
  left = len(secret_word) #  sätter "left" till hur många bokstäver det hemliga ordet har.
  guesses_left = 10 # Ger spelaren 10 liv
  used_letters = [] # sätter namnet så den kan användas senare som string


  # En loop som kollar om du har slut på gissningar eller ifall _ är lika som ordet
  while guesses_left > 0 and not dashes == secret_word:

    print(dashes) # Skriver ut dashes där bokstäverna är gömda.
    print("Bokstäver gissade: ", (used_letters)) # Skriver ut vilka bokstäver man gissat på.
    print ("Liv kvar: ", str(guesses_left)) # Skriver ut hut många gissningar man har kvar

    # frågar spelaren efter en gissning
    guess = input("Gissa:") # Skriver ut en fråga
    used_letters.append(guess) # Svaret man skriver byts ut ifall det stämmer med secret_word.

    if len(guess) != 1: # Ifall man inte skriver 1 bokstav så kör den det under.
      # Printar ut att man måste skriva en bokstav.
      print("") 
      print ("Din bokstav måste vara en bokstav!")

    # Ifall man gissar rätt så printar den det och sedan byter ut _ till bokstaven
    elif guess in secret_word:
      print("")
      print ("Du gissade en bokstav rätt!")
      dashes = update_dashes(secret_word, dashes, guess) # Uppdaterar dashes så man kan se vart bokstaven var i ordet.


    # Om spelaren gissar fel så säger programmet det och sedan tar bort ett liv från spelarn
    else:
      print("")
      print ("Du gissade fel.")
      guesses_left -= 1 # Tar -1 liv från guess_left.

    if guesses_left < 1: # När man har 0 guesses_left så printar den ut vad ordet var.
      print ("Du förlora, ordet var: " + str(secret_word))

  # Om _ är lika som ordet så har spelaren vunnit. Den printar också ut vad ordet var.
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
