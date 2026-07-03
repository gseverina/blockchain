# Especificación Técnica — Block

## Propósito

La clase `Block` representa la unidad básica de información de la blockchain educativa desarrollada en este proyecto.

Su objetivo es encapsular la información necesaria para formar parte de una cadena de bloques, manteniendo una interfaz simple y fácilmente extensible para las próximas etapas del curso.

---

# Responsabilidades

La clase deberá ser responsable de:

- Almacenar los datos asociados al bloque.
- Representar la posición que ocupa dentro de la cadena.
- Mantener una referencia al bloque inmediatamente anterior.
- Exponer la información necesaria para que otros componentes puedan interactuar con ella.

La clase **no** será responsable de validar la blockchain, calcular hashes, realizar minería ni ejecutar algoritmos de consenso.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear un bloque.
- Consultar la información almacenada.
- Consultar la posición del bloque.
- Conocer el bloque anterior.
- Tratar el bloque como un objeto conceptualmente inmutable después de su creación.

---

# Restricciones

En esta primera versión de la clase:

- No deberá calcular hashes.
- No deberá contener lógica de minería.
- No deberá conocer la blockchain completa.
- No deberá depender de bases de datos.
- No deberá depender de comunicación por red.
- No deberá depender de librerías específicas de blockchain.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir, justificando cada elección:

- Cómo representar los datos almacenados.
- Cómo representar la referencia al bloque anterior.
- Cómo representar la posición del bloque.
- Cómo implementar la inmutabilidad.
- Si utilizar una clase tradicional o `@dataclass`.
- Qué validaciones realizar durante la construcción del objeto.

No existe una única respuesta correcta para estas decisiones. Lo importante es que cada una tenga una justificación técnica.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Exista una clase `Block`.
- La clase cumpla todas las responsabilidades definidas en esta especificación.
- El código sea claro, legible y correctamente documentado.
- Las decisiones de diseño puedan ser explicadas y justificadas por el estudiante.

En esta etapa no se evaluará el rendimiento ni la optimización de la implementación.
