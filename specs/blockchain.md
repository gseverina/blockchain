# Especificación Técnica — Blockchain

## Propósito

La clase `Blockchain` representa la cadena de bloques del sistema.

Su responsabilidad es administrar la colección de bloques y ofrecer una interfaz simple para interactuar con ella.

La implementación deberá ser sencilla y servir como base para las próximas etapas del proyecto.

---

# Responsabilidades

La clase deberá ser responsable de:

- Mantener la colección de bloques.
- Permitir agregar nuevos bloques.
- Permitir consultar los bloques existentes.
- Preservar el orden de inserción de los bloques.

La clase **no** será responsable de:

- Validar bloques.
- Calcular hashes.
- Realizar minería.
- Resolver conflictos.
- Persistir información.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear una blockchain vacía.
- Agregar un bloque existente a la blockchain.
- Obtener la cantidad de bloques almacenados.
- Obtener un bloque por su posición dentro de la cadena.
- Recorrer todos los bloques de la blockchain.

---

# Restricciones

En esta primera versión:

- La implementación interna de la colección queda a criterio del estudiante.
- La blockchain no deberá modificar los bloques que almacena.
- La blockchain no deberá crear bloques automáticamente.
- La blockchain solo administrará objetos de tipo `Block`.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo almacenar internamente los bloques.
- Qué interfaz pública exponer.
- Cómo impedir que se agreguen objetos que no sean `Block`.
- Cómo manejar accesos fuera de rango al consultar un bloque.

No existe una única implementación correcta. Lo importante es que las decisiones respeten las responsabilidades definidas en esta especificación.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Exista una clase `Blockchain`.
- Sea posible crear una blockchain vacía.
- Sea posible agregar bloques existentes.
- La blockchain preserve el orden de los bloques.
- Solo puedan almacenarse objetos `Block`.
- El código sea claro, legible y correctamente documentado.

En esta etapa no se evaluará la validez criptográfica de la cadena ni la consistencia entre bloques.
