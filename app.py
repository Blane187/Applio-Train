import gradio as gr
import sys
import os

now_dir = os.getcwd()
sys.path.append(now_dir)

from tabs.inference.inference import inference_tab
from tabs.train.train import train_tab
from tabs.extra.extra import extra_tab
from tabs.report.report import report_tab
from tabs.download.download import download_tab
from tabs.tts.tts import tts_tab
from tabs.settings.presence import presence_tab

from assets.i18n.i18n import I18nAuto

i18n = I18nAuto()

from assets.discord_presence import RPCManager

RPCManager.start_presence()

with gr.Blocks(theme="Hev832/EasyAndCool", title="Applio Train") as Applio:
    gr.Markdown("# Applio Training ")
    gr.Markdown(
        i18n(
            "Ultimate voice cloning tool, meticulously optimized for unrivaled power, modularity, and user-friendly experience."
        )
    )
    gr.Markdown(
        i18n(
            "[Support](https://discord.gg/IAHispano) — [Discord Bot](https://discord.com/oauth2/authorize?client_id=1144714449563955302&permissions=1376674695271&scope=bot%20applications.commands) — [Find Voices](https://applio.org/models) — [GitHub](https://github.com/IAHispano/Applio)"
        )
    )
    

    with gr.Tab(i18n("Train")):
        train_tab()

    


if __name__ == "__main__":
    Applio.launch(debug=True, share=True)
