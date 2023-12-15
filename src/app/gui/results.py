from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class Result:
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
        self.canvas.place(x=0,y=0)
        
        self.logo_text = PhotoImage(
            file=self.relative_to_assets("logo_h.png"))
        self.logo_text_bg = self.canvas.create_image(
            165.0,
            58.0,
            image=self.logo_text
        )

        self.frame_left_img = PhotoImage(
            file=self.relative_to_assets("frame_l.png"))
        self.frame_left = self.canvas.create_image(
            352.0,
            433.0,
            image=self.frame_left_img
        )

        self.frame_right_img = PhotoImage(
            file=self.relative_to_assets("frame_r.png"))
        self.frame_right = self.canvas.create_image(
            912.0,
            433.0,
            image=self.frame_right_img
        )

        self.canvas.create_text(
            172.0,
            532.0,
            anchor="nw",
            text="C://Users/DELL/this/is/image/filepath.jpg",
            fill="#435585",
            font=("Consolas", 16 * -1)
        )

        self.title_text = PhotoImage(
            file=self.relative_to_assets("title.png"))
        self.title_text_bg = self.canvas.create_image(
            599.0,
            153.0,
            image=self.title_text
        )

        self.continue_bg = PhotoImage(
            file=self.relative_to_assets("btn__continue.png"))
        self.continue_btn = Button(
            image=self.continue_bg,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_continue,
            relief="flat",
            background="#FFFFFF"
        )
        self.continue_btn.place(
            x=492.0,
            y=678.0,
            width=216.0,
            height=72.0
        )

    def handle_continue(self):
        return
    
    def handle_link(self):
        return
    
    def handle_submit(self):
        return
        
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == '__main__':
    window = Tk()
    htr_app = Result(window=window)
    window.resizable(False,False)
    window.mainloop()