# Especificación Técnica — Integración Wallet / Transaction

## Propósito

Modificar la clase `Transaction` para que los participantes de una transacción sean objetos `Wallet` en lugar de cadenas.

---

# Responsabilidades

La clase `Transaction` deberá:

- Representar un emisor mediante una `Wallet`.
- Representar un receptor mediante una `Wallet`.
- Mantener las responsabilidades incorporadas en clases anteriores.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear una transacción entre dos wallets.
- Consultar ambas wallets.
- Comparar transacciones por contenido.

---

# Restricciones

La implementación:

- No deberá modificar la clase `Wallet`.
- No deberá modificar la clase `Blockchain`.
- No deberá modificar la clase `Block`.
- No deberá incorporar lógica criptográfica.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo validar que los participantes sean wallets.
- Cómo adaptar las validaciones existentes.
- Qué cambios realizar en la suite de tests.

No existe una única implementación correcta. Lo importante es que el modelo represente explícitamente que las transacciones ocurren entre wallets.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- `sender` sea una `Wallet`.
- `recipient` sea una `Wallet`.
- No sea posible crear una transacción con participantes inválidos.
- Continúen aplicándose las reglas de negocio definidas en la Clase 6.
- La suite de tests refleje correctamente el nuevo modelo.

