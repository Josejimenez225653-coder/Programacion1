def agregarCursos():
    curso={
        "nombre":input("Dime el nombre del curso: "),
        "instructor":input("Dime el nombre del instructor: "),
        "aula":input("Dime el aula del curso: "),
        "alumnos":{}
    }
    while True:
        alumno=input("Dime el nombre del alumno (o 'fin' para terminar): ")
        if alumno.lower().strip() == 'fin':
                break
        idalumno=input("Dime el id del alumno")
        
    curso["alumnos"][idalumno]["nombre"]=alumno
    curso={"nombre","instructor","aula","alumnos"}
        
        
        

    return curso