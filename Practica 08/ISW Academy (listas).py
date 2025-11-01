ListaCursos = []

def AnadirCurso():
    CursoNuevo = []
    print("Ha elegido añadir un curso.")
    CursoNuevo1 = input("Introduzca el nombre del Curso: ").capitalize()
    CursoNuevo.append(CursoNuevo1)

    InstructorNuevo = input("Introduzca el nombre del instructor: ").title()
    CursoNuevo.append(InstructorNuevo)

    AulaNueva = input("Introduzca el nombre del aula: ").capitalize()
    CursoNuevo.append(AulaNueva)

    CursoNuevo.append([])  
    ListaCursos.append(CursoNuevo)
    print(f"El curso fue añadido.")

def EliminarCurso():
    Nombre_curso_eliminar = input("Introduzca el nombre del curso que desea eliminar: ").capitalize()
    for curso in ListaCursos:
        
        if curso[0] == Nombre_curso_eliminar:
            ListaCursos.remove(curso)
            print(f"El curso {Nombre_curso_eliminar} ha sido eliminado.")
            return
    print("Curso no encontrado.")

def ModificarCurso():
    Nombre_curso_modificar = input("Introduzca el curso a modificar: ").capitalize()
    for curso4 in ListaCursos: 
        if curso4[0] == Nombre_curso_modificar:
            ListaCursos.remove(curso4)
    CursoNuevo = []
        
    CursoNuevo1 = input("Introduzca el nombre modificado del Curso: ").capitalize()
    CursoNuevo.append(CursoNuevo1)

    InstructorNuevo = input("Introduzca el nombre modificado del instructor: ").title()
    CursoNuevo.append(InstructorNuevo)

    AulaNueva = input("Introduzca el nombre modificado del aula: ").capitalize()
    CursoNuevo.append(AulaNueva)

    CursoNuevo.append([])  
    ListaCursos.append(CursoNuevo)
    print(f"El curso fue modificado.")
    return

def MostrarCursos():
    if not ListaCursos:
        print("No hay cursos registrados.")
    else:
        for listaC in ListaCursos:
            print(f"- {listaC}")

def AnadirAlumno():
    nombre_curso = input("Seleccione el curso en el que desea añadir al alumno: ").capitalize()
    alumno = input("Introduzca el nombre del alumno: ").title()
    for curso in ListaCursos:
        if curso[0] == nombre_curso:
            curso[3].append(alumno)
            print(f"Se ha añadido a {alumno} en el curso '{nombre_curso}'.")
            return
    print("Curso no encontrado.")

def EliminarAlumno():
    Nombre_curso_eliminar_Alumno = input("Introduzca el nombre del curso en el que desea eliminar al alumno: ").capitalize()
    for curso2 in ListaCursos:
        if curso2[0] == Nombre_curso_eliminar_Alumno:
            Alumno_a_eliminar = input("Introduzca el nombre del alumno a eliminar: ").title()
            for alumno in curso2:
                if alumno[0] == Alumno_a_eliminar:
                    curso2.remove(alumno)
                    print(f"El alumno {Alumno_a_eliminar} ha sido eliminado")

def MostrarLista():
    listaver = input("Introduzca el curso para ver su lista: ").capitalize()
    for curso3 in ListaCursos:
        if curso3[0] == listaver:
            for alu in curso3[-1]:
             print(f"- {alu}")

def menu():
    print()
    print("""°Ingeniería En Software Academy°
    Eliga la operación.
    1. Agregar curso
    2. Eliminar curso
    3. Modificar curso
    4. Mostrar todos los cursos
    5. Agregar alumno
    6. Eliminar alumno
    7. Mostrar lista de estudiantes
    8. Salir""")

while True:
    menu()
    opcion = int(input("Opción: "))

    match opcion:
        case 1:
            AnadirCurso()
        case 2:
            EliminarCurso()
        case 3:
            ModificarCurso()
        case 4:
            MostrarCursos()
        case 5:
            AnadirAlumno()
        case 6:
            EliminarAlumno()
        case 7:
            MostrarLista()
        case 8:
            print("Adiós. o/")
            break
        case _:
            print("Opción inválida.")