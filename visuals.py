def draw(choice):
    if choice == "rock":
        # Player chose rock, print rock
        return("""
           _____
        ---'   __)
              (___)
              (___)
              (__)
         ---.__(_)
        """)
    elif choice == "paper":
        # Player chose rock, print rock
        return("""
           _____
     ---'    __)____
                  ____)
                 _____)
                 _____)
        ---.__________)
     """)
    else:
        return("""
         _____
     ---'   __)____
                 ____)
             ________)
            (__)
       ---.__(_)
      """)
