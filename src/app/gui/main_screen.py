from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class MainHTR:
    def __init__(self, window) -> None:
        self.parent_path = Path(__file__).parent
        self.assets_path = self.parent_path / Path(f"../assets")

        self.window = window
        self.window.geometry("1200x800")
        self.window.configure(bg = "#FFFFFF")

        self.window.title("Handwritten Text Recognition")

        self.icon_path = PhotoImage(file=self.relative_to_assets("logo_h.png"))
        self.window.iconphoto(True, self.icon_path)

        self.canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 800,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        
        self.logo_text = PhotoImage(
            file=self.relative_to_assets("logo_h.png"))
        self.logo_text_bg = self.canvas.create_image(
            165.0,
            58.0,
            image=self.logo_text
        )

        self.canvas.place(x = 0, y = 0)
        self.frame_bg = PhotoImage(
            file=self.relative_to_assets("frame.png"))
        self.frame = self.canvas.create_image(
            600.0,
            433.0,
            image=self.frame_bg
        )

        self.img_image = PhotoImage(
            file=self.relative_to_assets("btn__image.png"))
        self.image_btn = Button(
            image=self.img_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_upload,
            relief="flat"
        )
        self.image_btn.place(
            x=494.0,
            y=359.0,
            width=213.0,
            height=136.0
        )

        self.img_upload = PhotoImage(
            file=self.relative_to_assets("btn__upload.png"))
        self.upload_btn = Button(
            image=self.img_upload,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_upload,
            relief="flat"
        )
        self.upload_btn.place(
            x=500.0,
            y=512.0,
            width=200.0,
            height=60.0
        )

        self.img_link = PhotoImage(
            file=self.relative_to_assets("btn__link.png"))
        self.link_btn = Button(
            image=self.img_link,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_link,
            relief="flat"
        )
        self.link_btn.place(
            x=707.0,
            y=512.0,
            width=60.0,
            height=60.0
        )

        self.img_submit = PhotoImage(
            file=self.relative_to_assets("btn__submit.png"))
        self.submit_btn = Button(
            image=self.img_submit,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_submit,
            relief="flat"
        )
        self.submit_btn.place(
            x=492.0,
            y=678.0,
            width=216.0,
            height=72.0
        )

        self.upload_text = PhotoImage(
            file=self.relative_to_assets("upload_y_img.png"))
        self.upload_text_bg = self.canvas.create_image(
            600.0,
            317.0,
            image=self.upload_text
        )

        self.title_text = PhotoImage(
            file=self.relative_to_assets("title.png"))
        self.title_text_bg = self.canvas.create_image(
            599.0,
            153.0,
            image=self.title_text
        )

    def handle_upload(self):
        return
    
    def handle_link(self):
        return
    
    def handle_submit(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from preview import Preview
        self.preview_gui = Preview(self.window)
        self.current_gui = self.preview_gui
        
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == '__main__':
    window = Tk()
    htr_app = MainHTR(window=window)
    window.resizable(False,False)
    window.mainloop()