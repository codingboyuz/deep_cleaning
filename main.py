import flet as ft
import os
import random
import string


class Service:
    @staticmethod
    def random_name(length=12):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def secure_delete(filepath, passes=5):
        if not os.path.isfile(filepath):
            return f"❌ Fayl topilmadi: {filepath}"

        dir_path = os.path.dirname(filepath)
        original_size = os.path.getsize(filepath)

        new_name = Service.random_name() + "." + Service.random_name(3)
        new_path = os.path.join(dir_path, new_name)
        os.rename(filepath, new_path)

        try:
            with open(new_path, 'r+b') as f:
                for _ in range(passes):
                    f.seek(0)
                    f.write(os.urandom(original_size))
                    f.flush()
                    os.fsync(f.fileno())
            os.remove(new_path)
            return f"✅ {os.path.basename(filepath)} o‘chirildi."
        except Exception as e:
            return f"❌ Xatolik: {filepath} - {e}"


class SecureFileDeleterApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Hard Delete"
        self.page.window.width = 350
        self.page.window.height = 350
        self.page.window.resizable = False
        self.page.window.max_width = 350
        self.page.window.max_height = 500
        self.page.window.min_width = 350
        self.page.window.min_height = 500
        self.page.bgcolor = "white"

        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.selected_files = []
        self.output_list = ft.ListView(auto_scroll=True, height=150)

        self.file_picker = ft.FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(self.file_picker)

        self.build_ui()

    def build_ui(self):
        self.page.add(
            ft.Column(
                [
                    ft.Column([
                        ft.ElevatedButton("📂 Fayllarni tanlash",
                                          on_click=lambda _: self.file_picker.pick_files(allow_multiple=True)),
                        ft.ElevatedButton("❌ Tanlangan fayllarni o‘chirish", color="white", bgcolor="red300",
                                          on_click=self.delete_files),
                    ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,  # vertikal markaz
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # gorizontal markaz
                    ),
                    ft.Container(content=self.output_list, border_radius=8,
                                 padding=5),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,  # vertikal markaz
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # gorizontal markaz
            )
        )

    def delete_single_file(self, filepath):
        result = Service.secure_delete(filepath, passes=5)
        self.selected_files.remove(filepath)
        self.refresh_output_list()

    def refresh_output_list(self):
        self.output_list.controls.clear()
        for f in self.selected_files:
            self.output_list.controls.append(
                ft.Row([
                    ft.Text(f"📄 {os.path.basename(f)}", expand=True),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color="red",
                        tooltip="Faylni o'chirish",
                        on_click=lambda e, path=f: self.delete_single_file(path)
                    )
                ])
            )
        self.page.update()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.selected_files.clear()
            self.selected_files.extend([f.path for f in e.files])
            self.refresh_output_list()
        else:
            self.output_list.controls.clear()
            self.output_list.controls.append(ft.Text("⚠️ Hech narsa tanlanmadi.", color="red"))
            self.page.update()

    def delete_files(self, e):

        if not self.selected_files:
            self.output_list.controls.append(ft.Text("⚠️ Avval fayllarni tanlang!", color="red"))
        else:
            self.output_list.controls.clear()

            for f in self.selected_files:
                result = Service.secure_delete(f, passes=5)
                self.output_list.controls.append(
                    ft.Text("O'chirildi", color='green' if result.startswith("✅") else "red")
                )
        self.page.update()


def main(page: ft.Page):
    SecureFileDeleterApp(page)


ft.app(target=main)
