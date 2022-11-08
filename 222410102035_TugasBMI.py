# Nama: Monica Caroline Gulo
# NIM: 222410102035
# Prodi: Teknologi Informasi

print("\n")
print("PENGHITUNGAN BODY MASS INDEX \n")

#input berat dan tinggi badan:
berat = float(input("Berapa berat badan Anda?(/kg): "))
tinggi = float(input("Berapa tinggi badan Anda?(/cm): "))

#konversi tinggi badan cm ke dalam m:
tinggi_input = tinggi/100

#rumus penghitungan BMI:
rumus = berat/(tinggi_input)**2

#pengujian:
if rumus < 18.5:
    print("Hasil penghitungan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: UNDERWEIGHT")
elif rumus >= 18.5 and rumus <= 24.9:
    print("Hasil penghitungan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: NORMAL WEIGHT")
elif rumus >= 25.0 and rumus <= 29.9:
    print("Hasil penghitugan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: OVERWEIGHT")
elif rumus >= 30.0 and rumus <= 34.9:
    print("Hasil penghitungan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: OBESITY CLASS I")
elif rumus >= 35.0 and rumus <= 39.9:
    print("Hasil penghitungan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: OBESITY CLASS II")
elif rumus >= 40.0:
    print("Hasil penghitungan BMI: ", round(rumus, 2))
    print("Keterangan IMT Anda adalah: OBESITY CLASS III")