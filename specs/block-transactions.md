# Especificación Técnica — Bloques con Transacciones

## Propósito

Modificar la clase `Block` para que almacene una colección de transacciones en lugar de datos arbitrarios.

---

# Responsabilidades

La clase `Block` deberá:

- Almacenar una colección de objetos `Transaction`.
- Mantener las responsabilidades incorporadas en clases anteriores.
- Continuar siendo inmutable.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear un bloque con cero o más transacciones.
- Consultar las transacciones almacenadas.
- Calcular el hash del bloque utilizando toda su información.

---

# Restricciones

La implementación:

- No deberá modificar la clase `Transaction`.
- No deberá modificar la clase `Wallet`.
- No deberá modificar la lógica de `Blockchain`.
- No deberá validar el contenido de las transacciones.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo representar la colección de transacciones.
- Si permitir bloques vacíos.
- Qué validaciones realizar durante la construcción del bloque.
- Cómo preservar la inmutabilidad de la colección.

No existe una única implementación correcta. Lo importante es que un bloque represente explícitamente una colección de transacciones.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- El atributo `data` haya sido eliminado.
- Exista un atributo que almacene transacciones.
- El bloque continúe siendo inmutable.
- El cálculo del hash siga reflejando el contenido completo del bloque.
- La suite de tests represente correctamente el nuevo modelo.

