# Especificación Técnica — Encadenamiento mediante Hashes

## Propósito

Modificar la representación de un bloque para que la relación con el bloque anterior se establezca mediante su hash, en lugar de una referencia directa al objeto.

---

# Responsabilidades

La clase `Block` deberá:

- Almacenar el hash del bloque anterior.
- Continuar representando un bloque individual dentro de la blockchain.
- Mantener la información necesaria para formar parte de una cadena.

La clase **no** será responsable de verificar que el hash almacenado sea correcto.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear un bloque génesis cuyo `previous_hash` sea inexistente.
- Crear bloques posteriores indicando el hash del bloque anterior.
- Consultar el valor de `previous_hash`.
- Calcular el hash del bloque como en la clase anterior.

---

# Restricciones

La implementación:

- Eliminará la dependencia directa entre bloques mediante referencias en memoria.
- No deberá almacenar objetos `Block` dentro de otro `Block`.
- No deberá validar la consistencia de la cadena.
- No deberá modificar el comportamiento de `Blockchain`.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo representar la ausencia de `previous_hash` en el bloque génesis.
- Cómo adaptar el cálculo del hash del bloque a la nueva estructura.
- Qué validaciones mantener durante la construcción del bloque.

No existe una única implementación correcta. Lo importante es que la relación entre bloques se establezca exclusivamente mediante hashes.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- El atributo `previous_block` haya sido eliminado.
- Exista un atributo `previous_hash`.
- El bloque génesis no requiera un `previous_hash`.
- Todo bloque posterior almacene un `previous_hash`.
- El cálculo del hash continúe funcionando correctamente con la nueva estructura.

