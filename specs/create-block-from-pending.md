# Especificación Técnica — Crear un Bloque desde las Transacciones Pendientes

## Propósito

Incorporar a `Blockchain` la capacidad de construir un nuevo bloque utilizando las transacciones pendientes.

---

# Responsabilidades

La clase `Blockchain` deberá ser responsable de:

- construir el siguiente bloque;
- asignar su índice;
- establecer el `previous_hash`;
- incorporarlo a la cadena;
- actualizar la colección de transacciones pendientes.

---

# Requisitos funcionales

La implementación deberá permitir:

- crear el bloque génesis automáticamente cuando la cadena esté vacía;
- crear bloques posteriores correctamente encadenados;
- mover todas las transacciones pendientes al nuevo bloque;
- dejar vacía la colección de transacciones pendientes después de crear el bloque.

---

# Restricciones

La implementación:

- no deberá modificar `Wallet`;
- no deberá modificar `Transaction`;
- no deberá modificar la estructura de `Block`;
- no deberá implementar minería.

---

# Decisiones abiertas

El estudiante deberá decidir:

- el nombre del método público;
- si el método devuelve el bloque creado;
- cómo reutilizar la lógica existente de `add_block()`;
- cómo vaciar la colección de transacciones pendientes de manera segura.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- la blockchain pueda crear un nuevo bloque sin recibir un `Block` externo;
- el índice del bloque sea correcto;
- el `previous_hash` sea correcto;
- las transacciones pendientes pasen al nuevo bloque;
- la colección de pendientes quede vacía;
- el nuevo bloque quede incorporado a la blockchain;
- todos los tests existentes continúen pasando.

