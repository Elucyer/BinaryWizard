import pandas as pd 

rutacompleta= r"C:\Users\Usuario\Desktop\perro\BinaryWizard\AGAVAL_ASIGNACION_22_05_2024_08_00_04.csv" 
rutacompleta2= r"C:\Users\Usuario\Desktop\perro\BinaryWizard\AGAVAL_ASIGNACION_22_05_2024_08_00_04.xls" 
df= pd.read_csv(rutacompleta, sep="|", on_bad_lines="skip")
#print(df)
#rutacompleta: lugar donde guarde el archivo
#sep: es la funcion de separador osea ",":";"|".";
#on_bad_lines: todo lo que al interior del archivo no este separado por | lo omite
#pd es el nombre que se la dataframe
#df.to_excel(rutacompleta2,index=False,engine="openpyxl")
#rutacompleta2: la ruta donde se va a guardar el archivo
#indix: indicador de posiciones 
#engine: motor de escritura de para archivos de excel

ruta= r"C:\Users\Usuario\Desktop\perro\BinaryWizard\holas.csv"
df= pd.read_csv(ruta,sep="|", on_bad_lines="skip")
#print(df)

datos={
    "Edad"   :[12,23,25],
    "Nombre" :["adrian","manuela","samanta"],
    "Sexo"   :["una vez por semana","nunca","soy virgen"],
    "Pais"   :["venezula","jamaica","italia"]
}
df_new= pd.DataFrame(datos)
Df_combinado=pd.concat([df,df_new],ignore_index=False)
Df_combinado=df_new
Df_combinado.to_csv(ruta,index=False,sep="|")
print(Df_combinado)





#Edad=[12,23,25]
#Nombre=["adrian","manuela","samanta"]
#Sexo=["una vez por semana","nunca","soy virgen"]
#Pais=["venezula","jamaica","italia"]

#df["Edad"]=Edad
#df["Nombre"]=Nombre
#df["Sexo"]=Sexo
#df["Pais"]=Pais

#df.to_csv(ruta,index=False,sep="|")
