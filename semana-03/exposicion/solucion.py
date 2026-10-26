# Esteban: Muestra el comportamiento por defecto (el "error" o texto feo)
class Estudiante:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad


estudiante1 = Estudiante("Santiago", 17)
print(estudiante1)
# Salida en consola: <__main__.Estudiante object at 0x...>
```[cite: 3]

---

# 2. Turno de Rodrigo : La solución con `__str__`
Pasas tú al teclado, agregas el método dunder `__str__` a la clase y ejecutas de nuevo para mostrar cómo se limpia el texto[cite: 3].

```python
# Rodrigo (Tú): Agrega __str__ para que sea legible por humanos
class Estudiante:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return f"Estudiante: {self.nombre}, Edad: {self.edad}"


estudiante1 = Estudiante("Santiago", 17)
print(estudiante1)
# Salida en consola: Estudiante: Santiago, Edad: 17
```[cite: 3]

---

### 👤 3. Turno de Santiago: `__str__` con condiciones
Pasa Santiago y demuestra que dentro de un dunder se puede programar lógica (como evaluar si un estudiante aprueba o reprueba según su nota)[cite: 3].

```python
# Santiago: Agrega lógica condicional dentro de __str__
class EstudianteNota:

  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def __str__(self):
    if self.nota >= 3.0:
      estado = "Aprobado"
    else:
      estado = "Reprobado"
    return f"{self.nombre} - Nota: {self.nota} - {estado}"


print(EstudianteNota("Carlos", 4.5))
print(EstudianteNota("Andrés", 2.5))
# Salida en consola:
# Carlos - Nota: 4.5 - Aprobado
# Andrés - Nota: 2.5 - Reprobado
```[cite: 3]

---

### 👤 4. Turno de Jhonathan : El método `__len__`
Cierra Jhonathan tipeando la clase `Grupo` para demostrar cómo el dunder `__len__` hace que el objeto funcione con la función nativa `len()`[cite: 3].

```python
# Jhonathan: Demuestra el uso de __len__ con una lista
class Grupo:

  def __init__(self, estudiantes):
    self.estudiantes = estudiantes

  def __len__(self):
    return len(self.estudiantes)


grupo = Grupo(["Sofía", "Carlos", "Andrés"])
print(len(grupo))
# Salida en consola: 3
```[cite: 3]

---

