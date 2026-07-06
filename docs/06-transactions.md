# Clase 6 — Transacciones

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué es una transacción dentro de una blockchain.
- Entender por qué una blockchain almacena transacciones y no simplemente datos arbitrarios.
- Identificar los componentes básicos de una transacción.
- Diseñar e implementar una primera versión de la clase `Transaction`.

---

# ¿Qué es una transacción?

Una blockchain no existe para almacenar bloques.

Existe para registrar información.

Esa información recibe el nombre de **transacción**.

Cada bloque agrupa una o más transacciones.

Podemos pensar en una blockchain como un gran libro contable donde cada bloque representa una página y cada transacción representa un asiento registrado en esa página.

---

# ¿Qué representa una transacción?

En términos generales, una transacción representa un cambio de estado.

Por ejemplo:

- Alice envía dinero a Bob.
- Un usuario registra la propiedad de un activo.
- Una organización certifica un documento.
- Se ejecuta un contrato inteligente.

Todas estas acciones son transacciones.

Nuestro proyecto comenzará con el caso más sencillo: una transferencia de valor entre dos participantes.

---

# Componentes básicos

En esta primera versión, una transacción estará compuesta por:

- Un emisor (`sender`).
- Un receptor (`recipient`).
- Un monto (`amount`).

Todavía no estudiaremos cómo demostrar que el emisor autorizó la operación.

Ese problema será resuelto cuando incorporemos firmas digitales.

---

# Inmutabilidad

Al igual que los bloques, una transacción representa un hecho ocurrido.

Una vez creada, no debería modificarse.

Por este motivo, nuestra implementación también será inmutable.

---

# Qué todavía NO estudiaremos

En esta clase no implementaremos:

- Firmas digitales.
- Wallets.
- Claves públicas.
- Criptografía asimétrica.
- Validación de balances.
- Comisiones.

El objetivo es únicamente modelar una transacción.

---

# Trabajo práctico

Diseñar e implementar la clase `Transaction`.

La implementación deberá representar una transferencia simple entre dos participantes.

Todavía no será utilizada por `Block`.

La integración entre bloques y transacciones será realizada en una clase posterior.

---

# Lo que aprenderemos en la próxima clase

Ahora que podemos representar una transacción, necesitaremos comprender quiénes participan de ella.

En la próxima clase construiremos nuestra primera representación de una wallet.

