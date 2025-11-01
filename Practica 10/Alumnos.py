import modelo.curso
from modelo.curso import agregarCursos

def agregarAlumno():
    alumnos={
        "Alumnos":{},
    }
    while True:
        alumno=input("Dime el nombre del alumno (o 'fin' para terminar): ")
        if alumno.lower().strip() == 'fin':
                break
        idalumno=input("Dime el id del alumno")
        
    agregarCursos["alumnos"][idalumno]["nombre"]=alumno
    alumnos["Alumnos"][len(alumnos["Alumnos"])+1]=alumno
          
    return alumnos 