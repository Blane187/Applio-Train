import gradio as gr
from core import run_model_information_script

from assets.i18n.i18n import I18nAuto

i18n = I18nAuto()


def model_information_tab():
    with gr.Column():
        model_name = gr.Textbox(
            label=i18n("Model Path"),
            placeholder=i18n("Introduce the model .pth path"),
            interactive=True,
        )
        model_information_output_info = gr.Textbox(
            label=i18n("Output Information"),
            value="",
            max_lines=8,
            interactive=False,
        )
        model_information_button = gr.Button(i18n("See Model Information"))
        model_information_button.click(
            run_model_information_script,
            [model_name],
            model_information_output_info,
            api_name="model_information",
        )
