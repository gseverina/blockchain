# Especificación Técnica — Wallet

## Propósito

Representar una identidad dentro de la blockchain.

Esta primera versión será deliberadamente simple y servirá como base para incorporar criptografía y firmas digitales en clases posteriores.

---

# Responsabilidades

La clase `Wallet` deberá:

- Representar una identidad.
- Ser inmutable.
- Poder compararse por su contenido.

---

# Requisitos funcionales

La implementación deberá permitir:

- Crear una wallet.
- Consultar su identificador.
- Comparar dos wallets.

---

# Restricciones

La implementación:

- No deberá generar claves criptográficas.
- No deberá almacenar balances.
- No deberá conocer transacciones.
- No deberá conocer bloques.
- No deberá conocer la blockchain.

---

# Decisiones abiertas

Durante la implementación, el estudiante deberá decidir y justificar:

- Cómo representar el identificador de una wallet.
- Qué validaciones realizar durante la construcción.
- Qué atributos forman parte de la identidad de una wallet.

No existe una única implementación correcta. Lo importante es que la clase represente una identidad del dominio y mantenga sus invariantes.

---

# Criterios de aceptación

La implementación se considerará completa cuando:

- Exista una clase `Wallet`.
- La clase sea inmutable.
- Toda wallet tenga un identificador.
- No sea posible crear wallets inconsistentes.
- Dos wallets con el mismo contenido sean consideradas iguales.

