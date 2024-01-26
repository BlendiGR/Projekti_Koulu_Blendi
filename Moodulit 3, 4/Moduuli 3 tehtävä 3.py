
sukupuoli = input("Mikä on sukupuolesi? (mies/nainen): ").lower()
hemoglobine = float(input("Mikä on hemoglobiini arvosi? (g/l): "))

def hemoglobine_tarkastaja(sukupuoli, hemoglobine):
    if sukupuoli not in ["mies", "nainen"]:
        print("Error. Sukupuolivaihtoehdot ovat vain mies tai nainen!")
    elif sukupuoli == "mies":
        if 134 <= hemoglobine <= 195:
            print("Hemoglobiini arvosi on OK!")
        elif hemoglobine < 134:
            print("Hemoglobiinisi on alhainen.")
        else:  # hemoglobine > 195
            print("Hemoglobiinisi on korkea.")
    elif sukupuoli == "nainen":
        if 117 <= hemoglobine <= 175:
            print("Hemoglobiini arvosi on OK!")
        elif hemoglobine < 117:
            print("Hemoglobiini arvosi on alhainen!")
        else:  # hemoglobine > 175
            print("Hemoglobiini arvosi on korkea.")

hemoglobine_tarkastaja(sukupuoli, hemoglobine)
