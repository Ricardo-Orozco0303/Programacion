print("Ingresa cual va hacer tu usuario")
Usuario = str(input())
print("Ingresa cual va hacer tu Contraseña")
Contraseña = str(input())
print("Por favor Ingresa tu Usuario Y contraseña")
print("Ingresa tu Usuario")
User = input()
print("Ingresa tu Contraseña")
Contraseña_ = input()
if Usuario == User and Contraseña == Contraseña_ :
  print("*******Bienvenido al sistema de fragmento de letras de canciones*******")
  print("Marca 1 para la letra de If I lose Myself")
  print("Marca 2 para la letra de payphone")
  print("Marca 3 para la letra de Story of my life ")
  print("Marca 4 para la letra de Under Control ")
  print("Ingresa un numero para continuar ")
  opcion = int(input())
  if opcion == 1 :
    print(" Fragmento de la cancion If I Lose Myself")
    print(" I stared up at the Sun \n", "Thought of all other people, places and things Ive loved \n", "I stared up just to see \n", "With all of the faces, you were the one next to me \n",
        "You can feel the light start to tremble \n", "Washing what you know out to sea \n", "You can see your life out the window,tonight \n")
  elif opcion == 2 :
    print(" Fragmento de la cancion payphone")
    print(" I'm at a payphone trying to call home \n", "All of my change I spent on you \n", "Where have the times gone? \n", "Baby, it's all wrong \n",
        "Where are the plans we made for two?")
  elif opcion == 3 :
    print(" Fragmento de la cancion Story of my life")
    print(" Written in these walls are the stories that I can't explain \n", "I leave my heart open but it stays right here empty for days \n",
        "She told me in the morning she don't feel the same about us in her bones \n", "It seems to me that when I die, these words will be written on my stone")
  elif opcion == 4 :
    print(" Fragmento de la cancion Under Control")
    print(" I might be anyone \n", "A lone fool out in the sun \n","Your heartbeat of solid gold \n", "I love you, you'll never know")
  else :
    print("Ingresa una valor valido")
else :
  print("Hubo un error en tu Usuario o contraseña")