i# Especificación Técnica — Validación de la Blockchain

## Propósito

Incorporar a la clase `Blockchain` la capacidad de verificar la integridad de la cadena mediante el encadenamiento de hashes.

---

# Responsabilidades

La clase `Blockchain` deberá ser capaz de:

- Recorrer todos los bloques almacenados.
- Verificar la relación entre bloques consecutivos.
- Determinar si la cadena es válida.

---

# Requisitos funcionales

La implementación deberá permitir:

- Validar una blockchain vacía.
- Validar una blockchain compuesta únicamente por el bloque génesis.
- Validar una blockchain con múltiples bloques correctamente encadenados.
- Detectar una inconsistencia entre `previous_hash` y el hash del bloque anterior.

---

# Restricciones

La implementación:

- No deberá modificar los bloques.
- No deberá recalcular ni corregir hashes almacenados.
- No deberá lanzar excepciones cuando la cadena sea inválida.
- Deberá devolver un resultado que indique si la blockchain es válida.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Si exponer la validación mediante un método o una propiedad.
- Cómo recorrer la cadena.
- Qué resultado devolver (`bool` u otra representación).

No existe una única implementación correcta. Lo importante es que la validación sea determinista y dependa únicamente del contenido de la blockchain.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Exista un mecanismo para validar la blockchain.
- Una blockchain vacía sea considerada válida.
- Una blockchain con un único bloque génesis sea considerada válida.
- Una blockchain correctamente encadenada sea considerada válida.
- Una blockchain con al menos un `previous_hash` incorrecto sea considerada inválida.
- La validación no modifique el contenido de la blockchain.

