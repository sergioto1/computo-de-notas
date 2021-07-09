'''
Un alumno desea saber cuál será su promedio general en las tres materias mas difíciles que
cursa y cuál será el promedio que obtendrá en cada una de ellas. Y además se desea saber
si paso o no el promedio de las tres asignaturas. El promedio se pasa con 3.0 y cada nota
está en el rango de 0 a 5.
En caso de no digitar código de materia correcto, debe informar “CODIGO DE FISICA NO
EXISTE o Matemática o Química” correspondiente y la nota de la materia será 0.0.
La función debe retornar una cadena, donde especifique si paso o no paso el promedio de las
materias con su correspondiente promedio.
'''

#codigo1 : str -> codigo materia matematica
#Exa1 : float -> nota examen matematica
#nota1 : float -> nota promedio tareas de matematica
#codigo2 : str -> codigo materia Fisica
#Exa2 : float -> nota examen Fisica
#nota2 : float -> nota promedio tareas de Fisica
#codigo3 : str -> codigo materia Quimica
#Exa3 : float -> nota examen Quimica
#nota3 : float -> nota promedio tareas de Quimica
def Promedio_Notas(codigo1:str, Exa1: float, nota1: float, codigo2:str, Exa2: float, nota2: float, codigo3:str, Exa3: float, nota3: float)->str:
    if (codigo1 == '111'):
        if (Exa1 >= 0.0 and Exa1 <= 5.0) and (nota1 >= 0.0 and nota1 <= 5.0):
            Mate = (Exa1 * 0.9)+(nota1 * 0.1)
    else:
        Mate = 0.0
        print ('CODIGO MATEMATCA NO EXISTE')
    
    if (codigo2 == '222'):
        if (Exa2 >= 0.0 and Exa2 <= 5.0) and (nota2 >= 0.0 and nota2 <= 5.0):
            Fis = (Exa2 * 0.8)+(nota2 * 0.2)
    else:
        Fis = 0.0
        print ('CODIGO FISICA NO EXISTE')
    
    if (codigo3 == '333'):
        if (Exa3 >= 0.0 and Exa3 <= 5.0) and (nota3 >= 0.0 and nota3 <= 5.0):
            Qui =(Exa3 * 0.85)+(nota3 * 0.15)
    else:
        Qui = 0.0
        print ('CODIGO QUIMICA NO EXISTE')
    
    promTotal = round(((Mate + Fis + Qui)/3),2)
    
    if (promTotal >= 3.0):
        return (f'paso el promedio con {promTotal}')
    else:
        return (f'No paso el promedio con {promTotal}')
    
# Pruebas

print(Promedio_Notas('111',3.0,3.0,'222',3.0,3.0,'333',3.0,3.0))
print(Promedio_Notas('111',4.0,3.0,'44',2.0,3.0,'333',2.2,2.0))
print(Promedio_Notas('11',4.0,2.0,'222',3.0,2.0,'333',2.8,2.0))
print(Promedio_Notas('111',4.0,2.0,'22',3.0,2.0,'33',2.8,2.0))
print(Promedio_Notas('111',4.0,3.0,'22',3.0,2.0,'33',2.8,2.0))
