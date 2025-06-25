#Diccionario
mime_tipo = {".gif": "image/gif",".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",".png":"image/png",
                ".pdf":"application/pdf",".txt":"text/plain",
                        ".zip":"application/zip"}

nombre_archivo = input("Ingrese nombre de archivo: ")
nombre_archivo = nombre_archivo.lower()
punto_extension = nombre_archivo.rfind('.')

if punto_extension == -1 or punto_extension == len(nombre_archivo) -1:
 tipo = "application/octet-stream"
else:
    extension = nombre_archivo[punto_extension:]  
    tipo = mime_tipo.get(extension, "application/octet-stream")

print("Tipo MIME:", tipo)