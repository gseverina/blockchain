# Clase 7 — Wallet

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué representa una wallet dentro de una blockchain.
- Diferenciar una persona de una identidad criptográfica.
- Entender por qué una wallet no almacena monedas.
- Diseñar una primera representación de una wallet.

---

# ¿Qué es una wallet?

Cuando alguien comienza a estudiar blockchain suele imaginar una wallet como una billetera física donde se guardan monedas.

En realidad, una wallet no almacena monedas.

Una wallet representa una identidad dentro de la blockchain.

Es esa identidad la que podrá crear transacciones, recibir activos y, más adelante, firmar digitalmente operaciones.

---

# ¿Qué contiene una wallet?

En una blockchain real, una wallet contiene mucha información relacionada con criptografía.

Sin embargo, todavía no estudiaremos esos conceptos.

En esta primera versión, una wallet tendrá únicamente un identificador que permita distinguirla de otras wallets.

Ese identificador representará nuestra identidad dentro de la blockchain.

---

# Wallet ≠ Persona

Es importante separar ambos conceptos.

Una persona puede tener múltiples wallets.

Una wallet puede dejar de utilizarse.

Una wallet puede incluso ser generada automáticamente por un programa.

Por eso, la blockchain no conoce personas.

Conoce únicamente wallets.

---

# ¿Por qué crear una clase Wallet?

Hasta ahora representamos los participantes de una transacción mediante cadenas de texto.

Eso fue suficiente para introducir el concepto de transacción.

Sin embargo, una cadena no expresa ninguna semántica.

Al crear una clase específica comenzamos a modelar explícitamente el dominio de nuestra blockchain.

---

# Qué todavía NO estudiaremos

En esta clase no implementaremos:

- Claves públicas.
- Claves privadas.
- Firmas digitales.
- Direcciones derivadas.
- Algoritmos criptográficos.
- Recuperación de wallets.

Nuestro objetivo es únicamente representar una identidad.

---

# Trabajo práctico

Diseñar e implementar una primera versión de la clase `Wallet`.

La implementación deberá representar una identidad única dentro de la blockchain.

Todavía no será utilizada por `Transaction`.

La integración entre ambos conceptos será realizada en la próxima clase.

---

# Lo que aprenderemos en la próxima clase

Ahora que existe una representación explícita de una wallet, reemplazaremos los participantes de las transacciones para que dejen de ser simples cadenas y pasen a ser identidades del dominio.

