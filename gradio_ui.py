import gradio as gr
from main import evaluate_startup

with gr.Blocks() as demo:
    gr.Markdown("### 🚀 Startup Idea Evaluator")
    with gr.Row():
        idea_input = gr.Textbox(label="Enter your Startup Idea", lines=4, placeholder="Your innovative idea goes here...")
    with gr.Row():
        submit = gr.Button("Evaluate")
        output = gr.Textbox(label="Evaluation Result", lines=10)

    submit.click(fn=evaluate_startup, inputs=idea_input, outputs=output)

demo.launch()