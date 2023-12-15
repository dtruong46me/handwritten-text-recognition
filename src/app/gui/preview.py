from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class Preview:
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
        self.frame_bg = PhotoImage(
            file=self.relative_to_assets("frame.png"))
        self.frame = self.canvas.create_image(
            600.0,
            433.0,
            image=self.frame_bg
        )
        
        self.logo_text = PhotoImage(
            file=self.relative_to_assets("logo_h.png"))
        self.logo_text_bg = self.canvas.create_image(
            165.0,
            58.0,
            image=self.logo_text
        )

        self.img_submit = PhotoImage(
            file=self.relative_to_assets("btn__submit.png"))
        self.submit_btn = Button(
            image=self.img_submit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_submit,
            relief="flat"
        )
        self.submit_btn.place(
            x=492.0,
            y=678.0,
            width=216.0,
            height=72.0
        )

        self.delete_img = PhotoImage(
            file=self.relative_to_assets("btn__delete.png"))
        self.delete_btn = Button(
            image=self.delete_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_delete,
            relief="flat",
            background="#FFFFFF"
        )
        self.delete_btn.place(
            x=573.0,
            y=567.0,
            width=54.0,
            height=54.0
        )

        self.title_text = PhotoImage(
            file=self.relative_to_assets("title.png"))
        self.title_text_bg = self.canvas.create_image(
            599.0,
            153.0,
            image=self.title_text
        )

        self.sample_bg = PhotoImage(
            file=self.relative_to_assets("sample_img.png"))
        self.sample_img = self.canvas.create_image(
            600.0,
            427.0,
            image=self.sample_bg
        )

        self.canvas.create_text(
            419.0,
            532.0,
            anchor="nw",
            text="C://Users/DELL/this/is/image/filepath.jpg",
            fill="#435585",
            font=("Consolas", 16 * -1)
        )

    def handle_upload(self):
        return
    
    def handle_link(self):
        return
    
    def handle_submit(self):
        return
    
    def handle_delete(self):
        return
        
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == '__main__':
    window = Tk()
    htr_app = Preview(window=window)
    window.resizable(False,False)
    window.mainloop()