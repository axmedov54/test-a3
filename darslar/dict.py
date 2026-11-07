

salon ={
    "Campanya":{
        "BMW":{
          "Model":"Model: M5 CS\nColor: Grey\n$123.000 to $127.400\n4.4L\n2023",
        },
       "Mercedes-Benz":{
            "Model":"M5",
            "Color":"Blue",
            "Price":"$300.000 to $340.000",
            "Engine_Displacoment":"4.3L",
            "Year":"2022",
        },
        "Porsche":{
           "Model":"911 Carrera", 
           "Color":"Grey",
           "Price":"$175 000 to $190 000",
           "Engine_Displacoment":"4.0 L",
           "Year":"2026"
        },
        "Lamborghini":{
            "Model":"Terzo Millennio",
            "Color":"Red",
            "Price":"300 000 to $900 000",
            "Engine_Displacoment":"V12",
            "Year":"2025",
        },
        "Tesla":{
            "Model":"Y Premium",
            "Color":"Green",
            "Price":"$25.000 to $50.000",
            "Engine_Displacoment":"V8",
            "Year":"2024",
        },
    }
}

for i in salon["Campanya"]:
    print(i ,end="\n")
    
user = input("Tallang ")

for j in salon["Campanya"][user]:
    print(j,end="\n")
    print("----------------")

user_m = input("Tallang ")

for m in salon["Campanya"][user][user_m]:
    print(m,end="")
   
    
















