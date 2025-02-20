import flet as ft
import asyncio

def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 840
    # UI Components
    timer_text = ft.Text("00:00", size=40, weight=ft.FontWeight.BOLD)
    minutes_input = ft.TextField(label="Minutes", value="0", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    seconds_input = ft.TextField(label="Seconds", value="0", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    start_button = ft.ElevatedButton("Start Timer", on_click=lambda e: page.run_task(start_timer, page, timer_text, minutes_input, seconds_input))

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row([minutes_input, seconds_input], alignment=ft.MainAxisAlignment.CENTER),
                start_button,
                timer_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

async def start_timer(page, timer_text, minutes_input, seconds_input):
    minutes = int(minutes_input.value)
    seconds = int(seconds_input.value)
    total_seconds = minutes * 60 + seconds

    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer_text.value = f"{mins:02d}:{secs:02d}"
        page.update()
        await asyncio.sleep(1)

    timer_text.value = "Time's up!"
    page.update()

ft.app(target=main)
