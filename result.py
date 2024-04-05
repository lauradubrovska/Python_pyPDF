import PyPDF2
result=0

try:
    file=input()

    if file!="":     
        row=[]
        pdf_file=PyPDF2.PdfReader(open(file,"rb"))
        number_of_pages=len(pdf_file.pages)
        page1=pdf_file.pages[0]
        page2=pdf_file.pages[1]
        text1=page1.extract_text()
        text2=page2.extract_text()
    
        pos1=text1.find("Elektroenerģija")
        pos2=text1.find("Elektroenerģijas papildpakalpojumi")
        apmaksai=text1[pos1+16:pos2]
        apmaksai=apmaksai.rstrip().replace("€","")
        apmaksai=apmaksai.replace(",",".")

        pos3=text2.find("EUR" + "\n" + "Elektroenerģija")
        pos4=text2.find("kWh")
        apjoms=text2[pos3+20:pos4]
        apjoms=apjoms.replace(",",".")
        apjoms=apjoms.replace(" ","").rstrip()

        pos5=text2.find("kWh")
        pos6=text2.find("Apkalpošanas maksa")
        
        d=text2[pos5+4:pos6].rstrip().replace(",",".")
        cenas=d.split(" ")
        cena=cenas[0]

        pos7=text1.find("Rēķina Nr.")
        datums=text1[pos7+10:pos7+20].rstrip()
        diena_beigas=int(datums[0:2])
        diena_sakums=int("01")
        menesis=int(datums[3:5])
        gads=int(datums[6:10])

        cena_float=float(cena)
        apmaksai_float=float(apmaksai)
        apjoms_float=float(apjoms)

        if apjoms_float==0:
            result=0
            print(result)

        else: 
            data=[]
            nordpool_price=[]
            cenu_sum=0
            with open("nordpool.csv","r") as f:
                for line in f:
                    row=line.rstrip().split(",")

                    price=row[2]
                    date=row[0]

                    if len(date) != 19:
                        continue

                    day=int(date[8:10])
                    month=int(date[5:7])
                    year=int(date[0:4])

                    if diena_sakums <= day <= diena_beigas and menesis == month and gads == year:
                        data.append(float(price))
                    
                        cenu_sum=sum(data)

            avg_cena=round(float(cenu_sum/len(data)),3)
            total=round(float(apjoms_float*avg_cena),3)
            result=round(((cena_float*apjoms_float)-(total)),1)
            print(result)
    else:
        result=0
        print(result)

except FileNotFoundError:
    result=0
    print(result)


