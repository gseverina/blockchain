# Proyecto: My Blockchain

## Visión del proyecto

**My Blockchain** es un proyecto educativo cuyo objetivo es construir una blockchain desde cero utilizando Python, avanzando de forma incremental y comprendiendo el propósito de cada uno de sus componentes.

No se trata de reproducir una implementación existente ni de desarrollar una criptomoneda lista para producción. El objetivo es aprender cómo se diseña una blockchain, por qué existen determinadas decisiones de arquitectura y qué problemas intenta resolver cada mecanismo que la compone.

Cada nueva característica será incorporada únicamente cuando el propio proyecto la necesite. De esta forma, el aprendizaje seguirá el mismo proceso que tendría un equipo de ingeniería al diseñar un sistema distribuido desde cero.

---

# Objetivos

Al finalizar este proyecto, el estudiante debería ser capaz de:

- Comprender la arquitectura general de una blockchain y el propósito de cada uno de sus componentes.
- Diseñar e implementar una blockchain funcional desde cero utilizando Python.
- Explicar las decisiones de diseño adoptadas durante la construcción del sistema.
- Analizar críticamente las diferencias entre una implementación educativa y plataformas reales como Bitcoin o Ethereum.
- Aplicar principios de ingeniería de software, incluyendo diseño incremental, testing, documentación y refactorización.

El objetivo no es memorizar conceptos, sino desarrollar la capacidad de razonar sobre ellos.

---

# Qué pretende enseñar

Este proyecto busca enseñar, entre otros temas:

- Diseño incremental de software.
- Estructuras de datos utilizadas en blockchain.
- Funciones hash.
- Criptografía aplicada.
- Firmas digitales.
- Bloques y cadenas de bloques.
- Prueba de trabajo (Proof of Work).
- Transacciones.
- Wallets.
- Modelos UTXO y Account.
- Redes P2P.
- Consenso distribuido.
- APIs para interactuar con una blockchain.
- Testing y validación del software.
- Buenas prácticas de ingeniería de software.

---

# Qué NO pretende enseñar

Este proyecto no pretende:

- Enseñar a invertir en criptomonedas.
- Explicar estrategias de trading.
- Construir una criptomoneda para producción.
- Desarrollar una blockchain con foco en rendimiento o escalabilidad.
- Aprender un framework específico de blockchain.
- Enseñar Solidity u otros lenguajes de contratos inteligentes desde el inicio.

El foco está puesto en comprender los fundamentos antes de utilizar herramientas existentes.

---

# Público objetivo

Este material está dirigido principalmente a:

- Estudiantes de informática.
- Desarrolladores de software.
- Docentes que deseen utilizar blockchain como herramienta educativa.
- Personas con conocimientos básicos de programación que quieran comprender cómo funciona una blockchain desde sus fundamentos.

Se asume familiaridad con programación en Python, pero no conocimientos previos sobre blockchain.

---

# Filosofía del proyecto

Este proyecto se apoya en algunos principios fundamentales.

## Comprender antes que copiar

Cada línea de código debe tener un propósito claro. El aprendizaje surge de comprender las decisiones de diseño, no de reproducir implementaciones existentes.

## Construcción incremental

El sistema crecerá paso a paso. Cada clase incorporará una única funcionalidad nueva, permitiendo comprender por qué aparece y cómo modifica el diseño existente.

## No implementamos nada cuya necesidad todavía no entendemos

Cada componente aparecerá únicamente cuando el propio proyecto lo necesite para resolver un problema concreto. De esta forma, la evolución del sistema será natural y cada decisión tendrá un motivo claramente identificable.

## La práctica guía la teoría

Los conceptos teóricos aparecerán cuando el proyecto los necesite. La teoría acompaña a la práctica y no al revés.

## Ingeniería de software

La blockchain será una excusa para aprender también diseño de software, testing, documentación, arquitectura y buenas prácticas de desarrollo.

---

# Metodología

Cada clase seguirá una estructura común:

1. Presentación del problema.
2. Introducción teórica.
3. Análisis y diseño.
4. Especificación funcional.
5. Implementación por parte del estudiante.
6. Verificación mediante tests.
7. Refactorización cuando sea necesaria.
8. Revisión técnica.
9. Reflexión sobre las decisiones tomadas.
10. Comparación con implementaciones reales.

El estudiante será responsable de escribir todo el código. El material del curso proporcionará la guía conceptual, las especificaciones funcionales y las preguntas necesarias para orientar el aprendizaje.

---

# Resultado esperado

Al finalizar el recorrido existirá un repositorio que contendrá:

- Una implementación completa de una blockchain educativa desarrollada en Python.
- Material didáctico organizado por clases.
- Diagramas y documentación técnica.
- Ejercicios y desafíos.
- Material reutilizable para estudiantes y docentes.

Más que un proyecto de programación, este repositorio documentará el proceso completo de diseñar, construir y comprender una blockchain desde sus fundamentos.

---

# Decisiones de diseño

## En esta clase se decidió

- El proyecto tendrá un enfoque completamente educativo.
- Todo el código será desarrollado por el estudiante.
- El material del curso actuará como guía, no como solución.
- La implementación crecerá de forma incremental.
- La documentación evolucionará junto con el código.
- Cada nueva característica deberá justificar su existencia resolviendo un problema previamente identificado.

## ¿Por qué?

El objetivo del proyecto es comprender el proceso de diseño de una blockchain, no simplemente reproducir una implementación existente. Documentar las decisiones de ingeniería permite comprender no solo qué se construyó, sino también por qué se eligió esa solución.

## Alternativas consideradas

- Desarrollar el proyecto siguiendo un tutorial tradicional.
- Construir una blockchain completa desde el primer momento.
- Basar el aprendizaje en un framework existente.

## ¿Por qué fueron descartadas?

Esas alternativas priorizan obtener un resultado funcional en menos tiempo, pero reducen significativamente la comprensión de las decisiones de diseño. En este proyecto se prioriza el aprendizaje profundo por sobre la velocidad de implementación.
