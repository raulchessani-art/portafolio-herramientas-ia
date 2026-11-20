from time import perf_counter

import gradio as gr
from transformers import pipeline

clasificador = pipeline(
    "image-classification",
    model="google/mobilenet_v2_1.0_224",
)


def clasificar(imagen):
    inicio = perf_counter()
    resultados = clasificador(imagen, top_k=3)
    duracion = perf_counter() - inicio
    etiquetas = {resultado["label"]: resultado["score"] for resultado in resultados}
    return etiquetas, f"{duracion:.2f} s"


app = gr.Interface(
    fn=clasificar,
    inputs=gr.Image(type="pil", label="Imagen"),
    outputs=[
        gr.Label(num_top_classes=3),
        gr.Textbox(label="Tiempo de clasificación (segundos)"),
    ],
    title="¿Qué hay en la foto?",
    description="Clasificación con el modelo google/mobilenet_v2_1.0_224.",
    examples=[
        ["ejemplos/carro.jpg"],
        ["ejemplos/mi-foto.jpg"],
    ],
)


if __name__ == "__main__":
    app.launch()
