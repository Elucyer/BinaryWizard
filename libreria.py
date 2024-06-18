import pandas as pd #importar la libreria

#rutacompleta = r"D:\Documentos\PROGRAMACION\PRUEBA_GIT\BinaryWizard\AGAVAL_ASIGNACION_22_05_2024_08_00_04.csv"
#rutacompleta2 = r"D:\Documentos\PROGRAMACION\PRUEBA_GIT\BinaryWizard\AGAVAL_ASIGNACION_22_05_2024_08_00_04.xlsx"

#df = pd.read_csv(rutacompleta, sep="|", on_bad_lines="skip")
#print(df)

#rutacompleta ------> la ruta donde estpa almacenado el archivo
#sep ---------> separador interno del archivo que puede ser "," ";" "|" "."
#on_bad_lines ----------> todo lo que no ste separado por | lo omite
#df ------------> es el nombre que se le da al dataframe

#df.to_excel(rutacompleta2, index=False, engine="openpyxl")
#rutacompleta2 ----------> la ruta donde se va a guardar el archivo
#index -----------> indicador de posiciones
#engine -----------> motor de escritura para archivos excel

ruta = r"D:\Documentos\PROGRAMACION\PRUEBA_GIT\BinaryWizard\hola.csv"
df = pd.read_csv(ruta, sep="|", on_bad_lines="skip")
print(df)

datos = {
    "Edad"      :[25,21,20], 
    "Nombre"    :["Luis","Pepito","Sara"],
    "Sexo"      :["NoBinario","Masculino","Pansexual"],
    "Pais"      :["Colombia", "Bolivia", "Ecuador"],
}

df_new = pd.DataFrame(datos)
df_existing = pd.read_csv(ruta, sep="|")
df_combinado = pd.concat([df_existing, df_new], ignore_index=True)
df_combinado = df_new

df_combinado.to_csv(ruta, index=False, sep="|")

print("Archivo actualizado, \n {df_combinado}")

#ruta -------> Directorio del archivo
#datos -----> Diccionario que contiene la informacion a agregar
#df_new -----> DataFrame -----> Libro de excel digital que se crea con la informacion
#df_existing ------> DataFrame que se crea con la informacion del archivo existente
#df_combinado -----> DataFrame que se crea al combinar la informacion del archivo existente y df_new
#ingnore_index -----> ingnora el indice de las filas
#to_csv ---------> metodo que permite escribir el archivo en extension csv