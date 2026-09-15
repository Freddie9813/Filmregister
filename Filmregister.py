

import film_modul 


film_register = [film_modul.Film("Inception"),
                 film_modul.Film("The Matrix"),
                 film_modul.Film("Interstellar")]


while True:
    

    print("\n---Filmregister---")

    print("1. Visa filmregister")
    print("2. Lägg till film i register: ")
    print("3. Sök efter film: ")
    print("4. Ta bort film: ")
    print("5. Avsluta")


    
    try:
        meny_val = int(input("Välj ett alternativ (1-5): "))
        

    except ValueError:
        
        film_modul.wrong_input()
        
        continue


##------Menyval 1------------------------------------------------------------------------------------------------------------------------------------
    if meny_val == 1:

        print("\n Filmregister:" )
        
        for film in film_register:
            
            print("\n", film.titel)


##------Menyval 2------------------------------------------------------------------------------------------------------------------------------------
    elif meny_val == 2:

        while True:
            film_add = input("\nAnge film att lägga till i registret eller tryck 'Enter' för att återgå till startmenyn: ")

            if film_add == "":

                print("\nÅtergår till startmeny")

                break


            elif film_add:
                
                ny_film = film_modul.Film(film_add)
                
                film_register.append(ny_film)
                
                print("\nDu har valt att lägga till : " + film_add)
                
                break

        
##------Menyval 3------------------------------------------------------------------------------------------------------------------------------------
    elif meny_val == 3:
        while True:
            
            film_search = input("\nAnge vilken film du söker efter eller tryck 'Enter' för att återgå till startmenyn: ") 


            if film_search == "":
                
                print("\n Återgår till startmeny")

                break
            

            found = False
            
            for film in film_register:
                                
                if film_search.lower() == film.titel.lower():
                    
                    found = True
                    
                    break
                
            
            if found:
                film_modul.film_found(film_search)
                
                            
            else:
                film_modul.film_not_found(film_search)


##------Menyva4 ------------------------------------------------------------------------------------------------------------------------------------
    elif meny_val == 4:

        while True:        
            film_search = input("\nAnge vilken film du vill ta bort eller tryck 'Enter' för att återgå till startmenyn: ")

            if film_search == "":
                
                print("\n Återgår till startmeny")

                break
            

            existing_film = False


            for film in film_register:
                
                if film_search.lower() == film.titel.lower():
                    
                    existing_film = film

                    break

            
            if existing_film:
                
                film_register.remove(existing_film)
                
                print(f"\nDu har valt att ta bort: {film_search}")            
                
                
            else:
                film_modul.film_not_found(film_search)

        
##------Menyval 5------------------------------------------------------------------------------------------------------------------------------------
    elif meny_val == 5:
        
        print("\nDu lämnar nu filmregistret. Hejdå!")
        
        break
        

    else:
        film_modul.wrong_input()








    
