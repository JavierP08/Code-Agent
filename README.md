# Code-Agent

Este repositorio contiene los archivos utilizados para implementar y evaluar un agente de software con modelos LLM usando [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) y [SWE-Bench](https://github.com/princeton-nlp/SWE-bench).

## Objetivo

El propósito de este proyecto es automatizar la resolución de *issues* de GitHub mediante un agente que interactúa con un modelo LLM (como Qwen) fine-tuneado para generar parches efectivos. Se evalúa el rendimiento del modelo utilizando el benchmark oficial de SWE-Bench.

## Contenido del repositorio

- **`ollama-finetune.py`**: Script en Python para subir un modelo fine-tuneado a Modal utilizando Ollama.
- **`ollama_modal.py`**: Script en Python para alojar el modelo base en Modal y configurar su endpoint para ser utilizado por SWE-Agent.
- **`qwen-finetune.yaml`**: Archivo de configuración en YAML para que SWE-Agent utilice el modelo desplegado en Modal (incluye parámetros como `api_base`, `model_name`, y `parse_function`).
- **`README.md`**: Este archivo.
- **`Google Colab del Fine-Tuning`**: El fine-tuning fue realizado en Google Colab. Aquí puedes ver el notebook donde se entrenó el modelo:
  [🔗 Google Colab - Fine-tuning Qwen con Unsloth](https://colab.research.google.com/) *(agrega aquí el enlace directo a tu notebook si ya lo publicaste)*

## Herramientas utilizadas

- **[SWE-Agent](https://github.com/princeton-nlp/SWE-agent)**: Herramienta para ejecutar agentes LLM que resuelven issues en repositorios de GitHub mediante generación de parches automatizados.
- **[SWE-Bench](https://github.com/princeton-nlp/SWE-bench)**: Benchmark utilizado para medir el rendimiento del agente, con múltiples tareas de evaluación y métricas como "fix coverage" y "pass@1".
- **[Modal](https://modal.com/)**: Plataforma utilizada para alojar tanto el modelo base como el modelo fine-tuneado de manera eficiente.
- **[Ollama](https://ollama.com/)**: Herramienta que permite trabajar con modelos en formato GGUF y exponerlos vía API compatible con SWE-Agent.
- **[Unsloth](https://github.com/unslothai/unsloth)**: Librería utilizada para realizar el fine-tuning del modelo (en este caso Qwen) de forma eficiente, incluso en entornos como Google Colab.

## Cómo comenzar

1. Realiza el fine-tuning de tu modelo siguiendo el notebook en Colab.
2. Usa `ollama-finetune.py` para cargar tu modelo fine-tuneado a Modal.
3. Usa `ollama_modal.py` si necesitas alojar un modelo base.
4. Configura tu agente con `qwen-finetune.yaml`.
5. Evalúa el desempeño con SWE-Bench (por ejemplo usando `run_evaluation`).

---

Si necesitas ayuda con la configuración o ejecución, puedes abrir un *issue* en este repositorio.

## Video:
- https://www.youtube.com/watch?v=-G_p4gRiJnw&feature=youtu.be
