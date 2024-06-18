import pandas as pd


#rutacompleta = r'C:\Users\USUARIO\Desktop\BinaryWizard\AGAVAL_ASIGNACION.csv'
#rutacompleta2 = r'C:\Users\USUARIO\Desktop\BinaryWizard\AGAVAL_ASIGNACION.xlsx'
#df = pd.read_csv(rutacompleta, sep='|', on_bad_lines='skip')
#rutacompleta -----> la ruta donde esta almacenado el archivo
#sep ----> el separador interno del archivo que pueden ser ",":";":"|":"."
#on_bad_lines  ---------> Todo lo que al interior del archivo no este separado por | lo omite
#df ------> es el nombre que se le da al dataframe
#df.to_excel(rutacompleta2, index=False, engine='openpyxl')
##rutacompleta2 ------> la ruta donde se va a guardar el archivo
## index ------> indicador de posiciones
## engine ------> motor de escritura para archivos excel

ruta = r'C:\Users\USUARIO\Desktop\BinaryWizard\holas.csv'

data = {
    'Edad': [25, 30, 22, 35],
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Sexo': ['M', 'F', 'M', 'F'],
    'Pais': ['Espana', 'Mexico', 'Argentina', 'Chile']
}

df_new = pd.DataFrame(data)

df_existing = pd.read_csv(ruta, sep='|')
df_combined = pd.concat([df_existing, df_new], ignore_index=True)
df_combined = df_new

df_combined.to_csv(ruta, index=False, sep='|')

print(f"Archivo CSV actualizado y lleno con éxito,\n {df_combined}")


#ruta -------> Directorio del archivo
#data ------> Diccionario que contiene la informacion a agregar
#df_new ------> DataFrame ----> libro de excel digital, que se crea con la informacion
#df_existing ------> DataFrame que se crea con la informacion del archivo existente
#df_combined ------> DataFrame que se crea al combinar la informacion del archivo existente y df_new
#ignore_index ------> ignora el indice de las filas
#to_csv ------> metodo que permite escribir el archivo en extension csv