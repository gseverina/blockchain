# Especificación Técnica — Transacciones Pendientes

## Propósito

Extender `Blockchain` para representar tanto los bloques confirmados como las transacciones pendientes.

---

# Responsabilidades

La clase `Blockchain` deberá administrar:

- la colección de bloques;
- la colección de transacciones pendientes.

No deberá crear bloques automáticamente.

---

# Requisitos funcionales

La implementación deberá permitir:

- registrar una nueva `Transaction` como pendiente;
- consultar las transacciones pendientes;
- conservar el orden de incorporación.

---

# Restricciones

La implementación:

- no deberá modificar `Wallet`;
- no deberá modificar `Transaction`;
- no deberá modificar `Block`;
- no deberá eliminar ninguna funcionalidad existente.

---

# Decisiones abiertas

El estudiante deberá decidir:

- cómo representar las transacciones pendientes;
- cómo exponerlas sin romper el encapsulamiento;
- qué validaciones realizar al incorporarlas.

No existe una única implementación correcta.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- `Blockchain` pueda almacenar transacciones pendientes;
- las transacciones mantengan el orden de incorporación;
- solo puedan agregarse objetos `Transaction`;
- la colección pueda consultarse desde el exterior sin comprometer la consistencia del objeto;
- todos los tests existentes continúen pasando.

