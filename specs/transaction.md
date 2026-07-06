# Especificación Técnica — Transaction

## Propósito

Representar una transacción simple entre dos participantes de la blockchain.

Esta primera versión tendrá únicamente fines educativos y servirá como base para incorporar autenticidad y firmas digitales en clases posteriores.

---

# Responsabilidades

La clase `Transaction` deberá:

- Representar un emisor.
- Representar un receptor.
- Representar un monto.
- Ser inmutable.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear una transacción.
- Consultar sus atributos.
- Comparar dos transacciones por su contenido.

---

# Restricciones

La implementación:

- No deberá realizar transferencias reales.
- No deberá verificar balances.
- No deberá utilizar criptografía.
- No deberá conocer la blockchain.
- No deberá conocer los bloques.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo representar a los participantes.
- Qué tipo utilizar para el monto.
- Qué validaciones realizar durante la construcción.

No existe una única implementación correcta. Lo importante es que la clase represente claramente una transacción y mantenga sus invariantes.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Exista una clase `Transaction`.
- La clase sea inmutable.
- Toda transacción tenga un emisor.
- Toda transacción tenga un receptor.
- Toda transacción tenga un monto.
- No sea posible crear transacciones inconsistentes.

