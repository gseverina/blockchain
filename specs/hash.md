# Especificación Técnica — Hash de un Block

## Propósito

Incorporar a la clase `Block` la capacidad de calcular una representación hash de su contenido utilizando SHA-256.

El hash identificará de forma única el estado del bloque en un momento determinado.

---

# Responsabilidades

La clase `Block` deberá ser capaz de:

- Obtener una representación estable de su contenido.
- Calcular el hash SHA-256 de esa representación.
- Devolver el hash en formato hexadecimal.

---

# Requisitos funcionales

La implementación deberá permitir:

- Calcular el hash de un bloque.
- Obtener siempre el mismo hash para un mismo bloque.
- Obtener hashes diferentes cuando cambie cualquier dato del bloque.

---

# Restricciones

La implementación:

- Deberá utilizar exclusivamente la biblioteca estándar de Python.
- No deberá depender de librerías externas.
- No deberá modificar el estado del bloque durante el cálculo.
- No deberá almacenar permanentemente el hash. Cada cálculo deberá obtenerse a partir del contenido actual del bloque.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo obtener una representación estable del contenido del bloque.
- Si exponer el hash mediante un método o una propiedad.
- Cómo serializar el contenido antes de calcular el hash.

No existe una única implementación correcta. Lo importante es que la representación utilizada sea determinista.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Sea posible obtener el hash de un bloque.
- Dos bloques con el mismo contenido produzcan el mismo hash.
- Una modificación en cualquiera de los datos del bloque produzca un hash diferente.
- El hash se represente como una cadena hexadecimal de 64 caracteres.
- El cálculo no modifique el estado del bloque.