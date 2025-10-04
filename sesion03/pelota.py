def envoltura(regalo):
    def papel():
        print("🎁🔖")
        regalo()
        print("🎁")
    return papel

def pelota():
    print("⚽")

pelota()

@envoltura
def pelota():
    print("⚽")

@envoltura
def chocolate():
    print ("🍫")

pelota()
chocolate()